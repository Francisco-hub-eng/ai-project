import os
from typing import Optional, Type, List

from pydantic import BaseModel, Field

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool, BaseToolkit

try:
    from swcpy import SWCClient
    from swcpy import SWCConfig
    from swcpy.swc_client import League, Team
except ImportError:
    raise ImportError(
        "swcpy is not installed. Please install it"
    )

config = SWCConfig(backoff=False)
local_swc_client = SWCClient(config)

class HealthCheckInput(BaseModel):
    pass

class HealthCheckTool(BaseTool):
    name: str = "HealthCheck"
    description: str = "useful to check if the API is running before you make other calls"
    args_schema: Type[HealthCheckInput] = HealthCheckInput
    return_direct: bool = False

    def _run(
            self, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool to check if the API is runnning."""
        health_check_response = local_swc_client.get_health_check()
        return health_check_response.text

class     
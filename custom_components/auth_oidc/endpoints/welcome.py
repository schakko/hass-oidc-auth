"""Welcome route to show the user the OIDC login button and give instructions."""

from aiohttp import web
from homeassistant.components.http import HomeAssistantView

PATH = "/auth/oidc/welcome"


class OIDCWelcomeView(HomeAssistantView):
    """OIDC Plugin Welcome View."""

    requires_auth = False
    url = PATH
    name = "auth:oidc:welcome"

    async def get(self, _: web.Request) -> web.Response:
        """Receive response."""

        return web.Response(
            headers={"content-type": "text/html"},
            text="<h1>OIDC Login</h1><p><a href='/auth/oidc/redirect'>Login with OIDC</a></p>",
        )
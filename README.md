# MCP-gotify

MCP server for sending gotify push notifications.

## Installation

### stdio

claude json:

```json5
{
    "mcpServers": {
        "mcp-gotify": {
            "command": "uvx",
            "args": ["mcp-gotify"],
            "env": {
                "GOTIFY_SERVER": "https://g.bvip.eu.org/", // Change this to your gotify server
                "GOTIFY_TOKEN": "An_pdhfU9X9W06p" // Get this from gotify
            }
        }
    }
}
```

### sse

```bash
git clone https://github.com/SecretiveShell/mcp-gotify
cd mcp-gotify
uv run mcp-gotify-sse
```

## License

MIT

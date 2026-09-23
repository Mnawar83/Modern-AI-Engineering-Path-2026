# Module 07 — Model Context Protocol (MCP)

## Goal

Expose reusable tools and data capabilities to AI hosts through a standard protocol.

## Learn

- host, client and server roles
- tools
- resources
- prompts
- capability discovery
- stdio vs network transports
- authentication and authorization
- least privilege
- server boundaries
- versioning and compatibility

## Why MCP matters

Without a protocol, every AI application invents its own connector layer. MCP makes a capability reusable across compatible AI hosts.

## Labs

1. Build a local MCP server exposing two read-only tools.
2. Add one resource containing reference data.
3. Add input validation and structured output.
4. Connect the server to an MCP-capable host.
5. Add a privileged write tool behind explicit authorization.
6. Document the trust boundary: what the host can access and what it cannot.

## 2026 note

The MCP ecosystem moves quickly. Check the current official SDK and specification before copying older tutorials; package names, transports and protocol versions can change.

## Done when

You can explain when an MCP server is better than adding a provider-specific tool integration directly inside one application.

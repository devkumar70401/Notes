# Zero Trust Security

**Core Philosophy**: "Never Trust, Always verify."

### 1. The Traditional Model: "Castle-and-Moat" (Outdated)

### 2. The Zero-Trust Model (Modern Standard)

- Zero-Trust assumes that threats exist both outside AND inside the network at all times.
- No user, microservice, device, or API call is trusted by default-even if it is inside the internal server farm.

## The 4 Technical Pillars of Zero-Trust

### 1. Least Privilege Access (ADTs & IAM)

- **Definition**: A user or service is granted only the absolute minimum permissions necessary to complete its task and nothing more.
- **Example**: Your web server process should have read-only access to specific database tables, never root OS permissions.

> **Detailed Master Blueprints**:
> - 📘 [Abstract Data Types (ADTs)](file:///home/dev/SE/Notes/10_CS_&_Engineering/12_DSA/01_Abstract_Data_Types.md) - Software abstraction contracts, encapsulation, and interface design.
> - 🛡️ [Identity and Access Management (IAM)](file:///home/dev/SE/Notes/10_CS_&_Engineering/15_System_Design/02_Identity_and_Access_Management.md) - Security authentication, authorization models (RBAC/ABAC), and policy evaluation engines.
---
layout: post
---
# SAML: A technical primer — SSOReady Docs
- URL: https://ssoready.com/docs/saml/saml-technical-primer
- Added At: 2024-12-11 09:24:45
- [Link To Text](_posts/2024-12-11-saml-a-technical-primer-—-ssoready-docs_raw.md)

## TL;DR
SAML（安全断言标记语言）是一种安全协议，用于实现单点登录和身份验证。它提供了一键登录体验，提高安全性和管理员工账户的便利性。SAML可以轻量化集成到现有软件中，使用XML独特化规范和签名验证来保证安全性。常见的身份提供者包括Okta、Microsoft Entra和Google Workspace。

## Summary
1. **SAML简介**：SAML（Security Assertion Markup Language）是一种安全断言标记语言，用于实现单点登录（SSO）和身份验证。

2. **SAML的目的**：
   - **用户体验**：提供一键登录体验，用户无需记忆多个密码。
   - **安全性**：让CISO（首席信息安全官）能够从单一位置控制和管理员工的所有账户。

3. **SAML在软件中的应用**：
   - **集成方式**：可以轻量化集成到现有软件中，只需要一小部分代码了解SAML。
   - **技术细节**：SAML协议的工作原理，安全保证和假设。

4. **SAML技术细节**：
   - **XML独特化**：用于规范化SAML消息的XML独特化过程。
   - **XML独特化规范**：XML独特化规范的要求和限制，包括实体扩展的安全问题。
   - **XML独特化参数**：InclusiveNamespaces PrefixList参数的使用和支持。

5. **SAML签名验证**：
   - **签名生成**：使用私钥生成签名的过程。
   - **签名验证**：使用公钥验证签名的过程，包括对签名值的计算和比较。

6. **SAML断言验证**：
   - **断言解析**：解析SAML断言的过程，包括验证断言的结构和内容。
   - **断言验证**：验证SAML断言的过程，包括检查断言的签名和内容。

7. **SAML身份提供者**：
   - **Okta**：Okta是一种流行的身份提供者，提供单点登录和身份验证服务。
   - **Microsoft Entra**：Microsoft Entra（以前称为Azure Active Directory）是一种身份提供者，提供单点登录和身份验证服务。
   - **Google Workspace**：Google Workspace是一种身份提供者，提供单点登录和身份验证服务。

8. **SAML安全性**：
   - **安全问题**：SAML协议的安全问题，包括XML实体扩展攻击。
   - **安全措施**：采取的安全措施，包括使用HTTPS和验证签名。

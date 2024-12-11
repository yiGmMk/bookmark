Title: SAML: A technical primer — SSOReady Docs

URL Source: https://ssoready.com/docs/saml/saml-technical-primer

Markdown Content:
If you just want to start integrating SAML right away, check out the [SAML quickstart](https://ssoready.com/docs/saml/saml-quickstart). You can get a SAML integration working end-to-end within a few hours.

This article is for folks who want to understand SAML at a deeper technical level, or how they could implement SAML without using an open-source library like SSOReady.

[SAML](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) (“Security Assertion Markup Language”) is a source of a lot of confusion for developers. This article is a technical primer on some of the most common questions engineers and other technical folks have about SAML:

1.  [Why do businesses want their software vendors to support SAML](https://ssoready.com/docs/saml/saml-technical-primer#what-is-the-point-of-saml)? In other words, how does SAML fit into my customer’s business? Why do end users and C-level executives at my customer care about SAML?
2.  [How should I fit SAML into my existing software](https://ssoready.com/docs/saml/saml-technical-primer#fitting-saml-into-your-existing-software)? What parts of my software stack need to be “SAML-aware”? How lightweight can I make my integration? (The answer: quite lightweight. Only a small part of your codebase needs to know about SAML at all.)
3.  [At a technical level, how does SAML even work](https://ssoready.com/docs/saml/saml-technical-primer#saml-at-a-technical-level)? What does the SAML protocol even do? What kinds of security guarantees does it give me, or what assumptions can I make about it?

What is the point of SAML?
--------------------------

Most likely, you’ll first hear about SAML because your customer wants your product to support it. Customer requests are the most common initial reason companies add support for SAML. But why does your customer want SAML support?

One click to login: why your users like SAML
--------------------------------------------

Your users probably don’t know what SAML is. What they do know about is their company’s _identity provider_. The most popular one is called [Okta](https://www.okta.com/customer-identity/single-sign-on/); other common competitors to Okta include [Microsoft Entra](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) (formerly “Azure Active Directory”) and [Google Workspace](https://workspace.google.com/). There are dozens more vendors in this space (big companies often build their own internal alternatives), and they all use the SAML protocol.

Even though your users don’t know what SAML or what an identity provider is, they do love what it gives them: one-click login experience for every SaaS tool they use at work, a so-called _Single Sign-On_ (SSO) experience.

For example, here’s what Okta looks like for your users. When your user opens their computer at work in the morning, this is what they see:

A screenshot of Okta. Every app they use at work gets a 'tile'. Click on a tile, and you're now logged into it.

At work, your users only need one password: their identity provider password. They don’t need to set up or remember passwords anywhere. They might find logging into Okta itself a bit annoying, because their IT team requires two-factor authentication to log into Okta, but logging into everything else is a breeze.

One click to fire: why your customer’s CISO likes SAML
------------------------------------------------------

A screenshot of an IT admin deprovisioning an Okta user. CISOs love SAML because it lets them lock down all of an employee's accounts from a single place.

Your customer’s [CISO](https://www.cisco.com/c/en/us/products/security/what-is-ciso.html) (Chief Information Security Officer) is in charge of making sure company data is secure. Concretely, the biggest things they worry about include:

*   Employees accidentally leaking data, because they use the same password everywhere and that password got breached
*   Employees intentionally leaking data, because they were fired and want revenge

CISOs love vendors that support SAML because they can put those vendor’s apps inside the corporate identity provider, e.g. Okta. From there:

*   Employees don’t need to have a password for that vendor. They just log in using the identity provider. The identity provider uses the SAML protocol to securely log the employee into the vendor’s app.
    
*   When the company fires someone, an IT admin doesn’t have to manually go in and delete that employee’s account from the vendor. Once you remove an employee from Okta, then the identity provider will stop letting that employee do SAML-based logins into _anything_. The fired employee is locked out of every work application.
    

But none of this works if your application doesn’t implement SAML. SAML is the protocol that powers single-sign on, which lets identity providers like Okta log employees into your app without using a password.

This is why many CISOs will go as far as to _require_ SAML support out of all vendors. Many companies have regulatory, contractual, or compliance obligations to ensure employees don’t use insecure passwords and are properly off-boarded after being fired. CISOs meet those obligations using SAML.

The “off-board employees after being fired” objective also pushes your customers toward wanting support for [SCIM](https://en.wikipedia.org/wiki/System_for_Cross-domain_Identity_Management). SAML lets your customers enforce “fired employees can’t log in again”, and SCIM additionally lets your customers enforce “fired employees’ accounts are automatically deactivated”.

The rest of this article is all about SAML, but [SSOReady can help you implement SCIM, too.](https://ssoready.com/docs/scim/scim-quickstart).

Fitting SAML into your existing software
----------------------------------------

If you read [the SAML specification](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf), or look at [documentation written about SAML](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) (especially if those docs were written in the early 2000s), it might seem like SAML is a framework that can subsume or replace all of auth. Don’t do this.

”SAML solves everything” was a hot idea in 2002, but the industry has moved away from this. The contemporary consensus is that SAML isn’t a great protocol. Just use SAML as a way to securely find out what a corporate user’s email address is.

You should think of SAML as a self-contained login method. You probably already let your users log into your product using things like username+password, email magic links, “Log in with Google”, etc. Think of SAML as another login method.

SAML is a protocol that lets your customer’s employees securely prove to you what their email address is, without you having to worry about sending them confirmation emails, verifying they’re still employed at the company, or that they belong to the right team at the company.

Roughly speaking, only two parts of your overall system need to know about SAML:

1.  Your login page needs to know that SAML is a login option for a customer. There are a couple common UI flows for doing this. We cover these in depth in the [Integrating SAML with your Login UI](https://ssoready.com/docs/saml/integrating-saml-into-your-login-ui) guide.
    
    Ultimately, your login page will, at a technical level, [initiate a SAML login](https://ssoready.com/docs/saml/saml-technical-primer#initiating-a-saml-login).
    
2.  Your login backend system needs to be able to [handle SAML assertions](https://ssoready.com/docs/saml/saml-technical-primer#handling-a-saml-assertion). We cover this in depth in the [Handling SAML Logins](https://ssoready.com/docs/saml/handling-saml-logins-jit-provisioning) guide.
    
    Ultimately your backend runs an HTTP endpoint, and your user’s web browsers will POST SAML payloads there. You verify those payloads, and use your normal session system (the same one you use for other kinds of logins) to create a session for the email you securely extracted from the SAML payload.
    

If you don’t use an open-source library like SSOReady to help implement SAML, the lack of structure that SAML imposes on you — as well as historical baggage from the early days of SAML — can lead you astray in two common ways:

1.  SAML supports the idea of putting “metadata” on a login session, configuring “conditional access”, and lots of other fancy functionality. It might seem like supporting SAML means having your entire system be able to honor these advanced SAML-specific features.
    
    Without getting into too much detail on what that functionality was meant to achieve in 2002, suffice it to say that most modern software systems don’t use this functionality at all.
    
    If you treat SAML as just a way to get a user’s email, you will be in line with almost all other SAML-supporting software your customer is used to. CISOs expect, and will be satisfied with, this kind of simple integration.
    
2.  SAML is, unfortunately, much more annoying to configure than any other login method you already support. The technical details of these SAML settings are covered later in this article [here](https://ssoready.com/docs/saml/saml-technical-primer#saml-configuration).
    
    You and your customer need to exchange settings about one another before a SAML login can even begin. But that configuration happens “offline” — if you’re not using SSOReady, you’ll implement it by exchanging informal emails with your customer. If you do use SSOReady, you can have your customer [self-serve configure their SAML setup](https://ssoready.com/docs/idp-configuration/enabling-self-service-configuration-for-your-customers).
    
    You don’t typically have to write any UI or backend code related to configuring SAML configuration, beyond having some way for your engineers to store the SAML settings you got from your customer. You just need to store three small pieces on your backend (two strings plus an X.509 certificate), and those settings change very infrequently.
    

SAML at a technical level
-------------------------

This section gets quite technical. You don’t need to understand this material to understand how to use SSOReady. This section is, in a way, a high-level overview of everything SSOReady abstracts away for you.

At the end of the day, SAML is a protocol that lets one of your users tell you (“assert”) their email address using a payload (an “assertion”) that is self-contained. When you get a SAML payload, you can securely know:

1.  Which of your corporate customers sent you the payload,
2.  What email address, according to that corporate customer, this user has
3.  That the corporate customer wants you to log this user in right away

The tricky part about SAML is that you need to watch out for:

1.  Forged SAML assertions, wherein an attacker pretends to be one of your corporate customers
2.  Malicious or misconfigured corporate customers sending assertions about other company’s employees, e.g. EvilCorp (`evilcorp.com`) telling you to log someone in as the CEO of AcmeCorp (`ceo@acmecorp.com`).

If you use SSOReady, these issues are both automatically covered by you. Otherwise, you’ll typically need to implement (2) yourself, and you may want to audit your SAML dependency to make sure they adequately handle (1). Sadly, securely authenticating SAML is tricky, and many libraries [don’t do it right](https://nvd.nist.gov/vuln/detail/CVE-2024-45409).

The SAML Flow
-------------

There are three actors involved in a SAML flow:

1.  You are the **service provider** (“SP”). The service provider is software product being logged into via SAML.
    
2.  Your customer’s Okta/Entra/Google/etc is the **identity provider** (“IDP”). The identity provider is responsible for knowing whether a user is a real employee that wants to log into a product, and for telling service providers about that information using SAML.
    
3.  The **user** is mostly just along for the ride. In SAML, the SP and the IDP will redirect the user to each other. The user’s browser is responsible for carrying messages back and forth between the SP and IDP.
    

A sequence diagram of a successful SAML login flow.

Logging in via SAML has five high-level steps:

1.  You and your customer agree, offline, on some settings about how you’re going to do SAML.
2.  When it’s time to log in via SAML, you have the user POST a SAML `AuthnRequest` to your customer’s identity provider. This is called “initiating” a SAML login.
3.  Your customer’s identity provider handles making sure the user really has valid corporate credentials. This step is entirely outside your app’s control.
4.  The identity provider has the user POST a SAML `Assertion` to your HTTP server.
5.  You authenticate that the assertion is legitimate, and then log the user into your product.

If you’re familiar with OAuth, this flow might sound familiar. The biggest difference between SAML and OAuth is how you verify the user after they get redirected back to your application.

In OAuth, your backend server typically takes a `code` from the user, and asks the identity provider if this `code` is legitimate, and what the underlying user’s details are if it is.

In SAML, your backend server never talks directly to the identity provider. You have to look at the assertion and use public-key cryptography to tell if the identity provider cryptographically signed the message.

Step (1) is important conceptually, but doesn’t require any code. That’s covered in the next section: [SAML Configuration](https://ssoready.com/docs/saml/saml-technical-primer#saml-configuration). Steps (2) and (5) are the ones you have to write code for. They’re covered in [Initiating a SAML Login](https://ssoready.com/docs/saml/saml-technical-primer#initiating-a-saml-login) and [Handling a SAML Assertion](https://ssoready.com/docs/saml/saml-technical-primer#handling-a-saml-assertion).

### SP- vs IDP-initiated SAML flows

The discussion above illustrates the “SP-initiated” SAML flow, where your application (the SP) decides to kick off the SAML flow.

SAML also supports “IDP-initiated” flows, where the IDP kicks off the SAML flow, and just directly sends the user to your ACS URL with an assertion.

A sequence diagram of a successful IDP-initiated flow.

The only difference between an SP- and an IDP-initiated flow is that IDP-initiated flows won’t require you to [initiate them](https://ssoready.com/docs/saml/saml-technical-primer#initiating-a-saml-login), and as a result don’t have [a `RelayState`](https://ssoready.com/docs/saml/saml-technical-primer#including-a-relaystate). Both are widely used in practice. When you use SSOReady, you get both SP- and IDP-initiated SAML support automatically.

SAML Configuration
------------------

For each of your customers, you will have five settings associated with the SAML connection you have with them. These settings are:

*   An **Assertion Consumer Service (“ACS”) URL**. You assign this value. It’s a URL where you run an HTTP endpoint that’s ready to [handle SAML assertions](https://ssoready.com/docs/saml/saml-technical-primer#handling-a-saml-assertion). When the identity provider redirects the user back to your application, they’ll send the user to the ACS URL.
    
*   An **SP Entity ID**. You assign this value, and it must be unique for every customer. It’s a generic string, but conventionally it’s formatted as a URL. The identity provider will include this SP Entity ID in the assertions it sends you, and you’ll use it to ensure the assertion was meant for _you_ and not some other application.
    
*   An **IDP Redirect URL**. The IDP assigns this value. When you [initiate a SAML login](https://ssoready.com/docs/saml/saml-technical-primer#initiating-a-saml-login), this is the URL you redirect the user to.
    
*   An **IDP Entity ID**. The IDP assigns this value. It’s a generic string, but conventionally it’s formatted as a URL. When you initiate a SAML login, you include this value so the IDP knows which application is starting the login. The IDP will include this IDP Entity ID in the assertions it sends you, and you’ll use it to make sure the assertion is coming from the right identity provider.
    
*   An **IDP Certificate**. The IDP assigns this value. The IDP will use this certificate to cryptographically sign the assertions it sends you. You will use this certificate to authenticate that the identity provider really generated the assertion, and that it wasn’t forged or tampered with.
    

Once you have all of these settings in place, you can begin doing SAML logins.

Initiating a SAML Login
-----------------------

Initiating a SAML login concretely consists of having your user’s web browser send a POST request with a payload that looks like this:

The `Issuer` needs to be equal to the [SP Entity ID](https://ssoready.com/docs/saml/saml-technical-primer#saml-configuration).

That POST request needs to be pointed at the [IDP Redirect URL](https://ssoready.com/docs/saml/saml-technical-primer#saml-configuration). The POST request needs to be a standard HTTP form, with the `AuthnRequest.xml` being base64-encoded and set as a form field called `SAMLRequest`.

You can’t use a normal HTTP redirect to have your user POST a form to another URL. The typical workaround is to render your user a form that self-submits using JavaScript:

Self-Submitting SAML Initiation Form

### Including a `RelayState`

When initiating a SAML login, you can optionally include a `RelayState` parameter. You include this data as an additional parameter in the POST request:

Self-Submitting SAML Initiation Form with a RelayState

Whatever you put in `RelayState` will be echoed back to you when you [handle the SAML assertion](https://ssoready.com/docs/saml/saml-technical-primer#handling-a-saml-assertion). The HTTP POST you receive will contain, alongside the usual `SAMLResponse` entry, a `RelayState` entry.

The typical use-case for `RelayState` is to keep track of what page your user was on before forced them to log in with SAML. Then, once they’re done logging in with SAML, you redirect the user back to the page they were previously on.

You can’t trust that the `RelayState` you get back from an identity provider is the same as the one you chose when initiating the SAML login. An attacker can always send you a request with their own `RelayState` instead.

The most common security risk associated with `RelayState` is when you store a URL in that `RelayState`, but don’t authenticate its legitimacy. If the `RelayState` is allowed to redirect to a URL outside of your web application, then you have an [open redirect vulnerability](https://cwe.mitre.org/data/definitions/601.html).

The safest solution is to cryptographically sign the `RelayState` value you include in your request using a secret key. When you use SSOReady, every `RelayState` is cryptographically authenticated; you do not need to worry about the [`state` parameter](https://ssoready.com/docs/ssoready-concepts/saml-login-flows#state) being tampered with.

Handling a SAML Assertion
-------------------------

After you [initiate a SAML login](https://ssoready.com/docs/saml/saml-technical-primer#initiating-a-saml-login), the user is now on the identity provider’s website. The user then identifies themselves to the identity provider. Exactly how this works is outside of your control.

Typically, an identity provider will ask for a user’s password, and then may do multi-factor authentication checks. The point of SAML is that your customer’s IT admin decides on their corporate security policy, and their identity provider implements the logic. Your application doesn’t need to worry about it.

If the identity provider decides to not proceed — maybe the user is fired, or maybe hasn’t been internally authorized to use your application (e.g. your customer only wants engineers using your app, but the employee works in sales), then from your perspective, nothing happens. You’ll never hear back from the login attempt. SAML doesn’t have a “login attempt failed” mechanism.

But if the login succeeds, then your user’s web browser will be redirected back to your [SAML ACS URL](https://ssoready.com/docs/saml/saml-technical-primer#saml-configuration). The user will POST you a standard set of HTML form data. That form data will contain up to two values:

*   A `SAMLResponse` element, containing a base64-encoded XML document. This is the SAML assertion.
*   A `RelayState`. This is only included if you [included a `RelayState` in your initiation request](https://ssoready.com/docs/saml/saml-technical-primer#including-a-relaystate).

The job of “handling a SAML login” consists of three steps:

1.  Authenticating the legitimacy of the SAML payload
2.  Deciding whether you want to honor the SAML request
3.  Logging the user in

To do any of this, you first need to parse the SAML assertion, and make sense of its contents.

### Anatomy of a SAML assertion

The previous section discusses how your [ACS URL](https://ssoready.com/docs/saml/saml-technical-primer#saml-configuration) will receive an HTML form with a `SAMLResponse`. Here’s a real example of such a `SAMLResponse`, base64-decoded, that came from Okta:

When we later [authenticate the SAML assertion](https://ssoready.com/docs/saml/saml-technical-primer#cryptographically-authenticating-a-saml-assertion), this is the payload we will be authenticating. Whitespace matters.

But for the purposes of human legibility, let’s look at it in a prettier form:

assertion.xml (Pretty-Indented)

The most important pieces of information are:

*   The assertion **issuer** lives in `<saml2:Issuer>`
    
*   The assertion **signature** lives in `<ds:Signature>` (specifically the one inside `<saml2:Assertion>`). The most important parts are the
    
    *   Canonicalization `Algorithm` on `<ds:CanonicalizationMethod>`
    *   Signature `Algorithm` on `<ds:SignatureMethod>`
    *   Digest `Algorithm` on `<ds:DigestMethod>`
    *   The digest hash in `<ds:DigestValue>`
    *   The signature value in `<ds:SignatureValue>`
*   The assertion **subject ID** lives in `<saml2:NameID>`
    
*   The assertion’s **validity window** is specified by the `NotBefore` and `NotOnOrAfter` on `<saml2:Conditions>`
    
*   The assertion’s **audience** lives in `<saml2:Audience>`
    

Validating the assertion signature is what [cryptographically authenticating a SAML assertion](https://ssoready.com/docs/saml/saml-technical-primer#cryptographically-authenticating-a-saml-assertion) is all about. Validating all the other pieces of information — the issuer, the subject ID, the validity window, the audience — happens when you [decide whether to honor the login](https://ssoready.com/docs/saml/saml-technical-primer#deciding-whether-to-honor-a-saml-login).

### Cryptographically authenticating a SAML assertion

Cryptographically authenticating SAML assertions is the most perilous part of implementing SAML. This is the step where the most security-critical mistakes happen.

If you choose to implement this yourself, you’re going to at minimum have to handle untrusted XML payloads. Make sure your code (and its dependencies) aren’t susceptible to generic XML vulnerabilities like [billion laughs](https://cwe.mitre.org/data/definitions/776.html) and [XML entity expansion attacks](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing).

From there, you’ll need to implement [XML Signature (aka XMLDsig)](https://www.w3.org/TR/xmldsig-core/). This section will call out many of the more common vulnerabilities with XML Signature implementations.

Before you can process a SAML assertion, you need to verify that it was really sent by your customer’s identity provider. You **must** do this, because the SAML assertion comes from an untrusted source: a user’s browser. How do you know the user’s request contains a SAML assertion that was really produced by your customer’s identity provider?

Make sure your SAML implementation can’t be tricked into skipping the process of cryptographically authenticating SAML assertions.

Many SAML implementations can have such checks trivially bypassed by, for example, just removing the `<ds:Signature />` elements in an assertion. This attack works most often when code contains logic that merely asks “are there any invalid signatures in this XML payload?“. A SAML assertion without any signatures trivially passes such a check.

[SSOReady always requires that SAML assertions be signed](https://ssoready.com/docs/ssoready-concepts/saml-login-flows#unsigned-assertion). This functionality cannot be disabled.

SAML implements cryptographic authentication using [XML Signature](https://www.w3.org/TR/xmldsig-core/), which is a very complicated standard that tries to anticipate dozens of different ways to sign XML messages. Thankfully, the SAML specification does restrict what parts of XML Signature can be used in a SAML assertion:

> 5.4 XML Signature Profile
> 
> \[…\] This section details constraints on these facilities so that SAML processors do not have to deal with the full generality of XML Signature processing.

The restrictions SAML imposes on XML Signature are:

*   XML Signature supports many different ways for where to put a signature relative to what it signs. SAML assertions are signed using _enveloped_ signatures. This means the `<ds:Signature />` elements in a SAML assertion are placed _inside_ the assertion.

The same section of the specification reads:

> SAML processors SHOULD support the use of RSA signing and verification for public key operations in accordance with the algorithm identified by `http://www.w3.org/2000/09/xmldsig#rsa-sha1`.

Do not implement this requirement. Require `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256` instead.

SHA1 was still considered secure when SAML 2.0 was drafted, but it is not considered secure today. In practice, all modern identity providers support RSA-SHA256 at minimum instead.

*   XML Signature supports many different ways for a signature to indicate what it’s signing. SAML stipulates that every assertion must have an `ID="..."` attribute, and that the signature points at it using `URI="#..."`.
    
*   XML Signature supports many _canonicalization_ algorithms (more on these later). SAML assertions always use [Exclusive XML Canonicalization](https://www.w3.org/TR/xml-exc-c14n/).
    

SAML authenticates data in a three-step process: a subset of the SAML assertion gets _canonicalized_ and then _digested_ (i.e. hashed). The hash is then _signed_ using RSA.

More concretely, the steps are to:

1.  [Extract out the data that we want to canonicalize](https://ssoready.com/docs/saml/saml-technical-primer#extracting-the-saml-assertion-to-authenticate)
2.  [Canonicalize that data](https://ssoready.com/docs/saml/saml-technical-primer#canonicalizing-a-saml-assertion)
3.  [Verify the digest (i.e. hash) of the canonicalized data](https://ssoready.com/docs/saml/saml-technical-primer#verifying-the-digest-of-the-canonicalized-assertion)
4.  [Extract out the data we want to sign](https://ssoready.com/docs/saml/saml-technical-primer#extracting-the-signedinfo-to-sign)
5.  [Verify the RSA signature of that data](https://ssoready.com/docs/saml/saml-technical-primer#authenticating-the-signedinfo)

The data to authenticate is the `<saml2:Assertion>` inside the overall `<saml2p:Response>` payload, but with the `<ds:Signature>` element removed. However, you may need to copy over namespace declarations from the top-level `<saml2p:Response>`; for instance, the identity provider [Keycloak](https://www.keycloak.org/) shapes its assertions like so:

You don’t sign `<saml:Assertion>...</saml:Assertion>`. You have to copy over all namespaces “above” the XML assertion that are [“visibly utilized”](https://www.w3.org/TR/xml-exc-c14n/#def-visibly-utilizes), including in this case the `xmlns:saml` declaration:

With this data in hand, you are ready to canonicalize the assertion.

#### Canonicalizing a SAML assertion

From there, you have to carry out the [Exclusive XML Canonicalization](https://www.w3.org/TR/xml-exc-c14n/) algorithm on the assertion. This algorithm is hairy in the details, but at a high level it is there to make operations like “remove the `<Signature>` element from the `<Assertion>`” be something that two parties can carry out, and still end up with exactly the same set of bytes. Canonicalization (“c14n”) is an XML-to-bytes algorithm.

Many XML libraries have abstractions that make it impossible to implement XML canonicalization. You may need to write your own XML parser.

You need to use a library that exposes where XML namespaces are declared (i.e. `xmlns:` attributes), and which lets you see what namespace prefixes (i.e. the `foo` in `foo:bar`, not just what `foo` resolves to) that elements and attributes use. These details are often abstracted away, because they don’t affect message semantics.

Exclusive XML Canonicalization builds on top of [Canonical XML](https://www.w3.org/TR/xml-c14n11/), aka “XML Canonicalization” or just “XML c14n”.

XML Canonicalization is rather involved, but the basic idea is to make details that don’t affect message semantics always resolve to the same thing:

*   Empty elements (`<foo />`) are converted to start/end pairs (`<foo></foo>`)
*   Element attributes are sorted by resolved namespace URI, ties broken alphabetically. Namespace declarations come first.
*   Whitespace within elements is removed, but whitespace in text nodes is preserved

The XML canonicalization spec is written to [require support for entity expansion](https://www.w3.org/TR/2001/REC-xml-c14n-20010315#Example-Entities), for instance requiring that this document:

Input.xml (from the XML Canonicalization specification)

Canonicalize to:

**Do not honor this requirement.** You will be vulnerable to [XML Entity Expansion (“XXE”)](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing) attacks. The specification here is simply inappropriate for systems that handle untrusted user input, such as SAML. In the real world, no SAML systems rely on entity expansion. This part of the spec is irrelevant and actively insecure in practice.

What makes XML Exclusive Canonicalization different from ordinary XML Canonicalization is in how XML namespaces are handled. In particular, XML Canonicalization stipulates that you only include XML namespaces that are [_visibly utilized_](https://www.w3.org/TR/xml-exc-c14n/#def-visibly-utilizes).

In other words, you take every namespace declaration (e.g. a `xmlns:foo="bar"` attribute), and you scan through everything “inside” that element. If they use the declared namespace prefix (e.g. `<foo />` or `foo:lorem="ipsum"`), then you keep the namespace declaration. Otherwise, you omit it from the output. If a namespace declaration is “shadowed” (i.e. redeclared by a child element), then you need to make sure it’s not the child declaration that’s being used. If two prefixes resolve to the same URI (e.g. `<lorem xmlns:a="xxx" xmlns:b="xxx">`), you need to track the prefixes independently.

XML Exclusive Canonicalization permits for an [`InclusiveNamespaces PrefixList`](https://www.w3.org/TR/xml-exc-c14n/#def-InclusiveNamespaces-PrefixList) parameter. You need to support this. In SAML, that parameter gets passed in a `InclusiveNamespaces` attribute under the `ds:Transform` element for canonicalization in the signature:

What this element concretely does is say that any declaration of `xs` (e.g. `xmlns:xs="..."`) is always treated as being visibly used.

The XML Exclusive Canonicalization spec has a bunch of discussion about special-casing `xmlns=""`. You don’t need to worry about this; it’s written to make the spec easier to implement using XPath, which has a hard time “seeing” `xmlns=""` declarations. But such declarations are never used in practice in SAML.

You do, however, need to handle checking whether default (i.e. unprefixed) namespace declarations are visibly used. Many identity providers send assertions that declare default namespaces. Not all of these declarations are always visibly used.

When you’re done with this step, you’ve converted the SAML payload into a precise sequence of bytes, representing a normalized (i.e. canonicalized) representation of the payload’s `<Assertion>` with the `<Signature>` removed. Now, we can move on to doing cryptography.

#### Verifying the digest of the canonicalized assertion

After converting the SAML assertion into a set of canonicalized bytes, SAML requires
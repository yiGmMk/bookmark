Title: How does Ory compare to alternatives like e.g. Keycloak and Authelia? From exper...

URL Source: https://news.ycombinator.com/item?id=25763320

Markdown Content:
	Hacker News new | past | comments | ask | show | jobs | submit	login



	
	
ralala on Jan 13, 2021 | parent | context | favorite | on: Ory Hydra 1.9: Open-source Golang OAuth2 provider


How does Ory compare to alternatives like e.g. Keycloak and Authelia?

From experience, can anyone make a recommendation for a system that can be rolled out to an organization with confidence (long-term support, security, performance)?




	
	
_hackerman on Jan 13, 2021 | next [–]


Keycloak and Authelia try to solve everything at once. So you get user management, but you also need to use their template and plugin system (so Java for Keycloak) and you can't use a different OAuth2 provider because well - you use Keycloak. I really love the projects and they have their use cases - with Ory however, you simply pick what you need:

- Login, registration, mfa, user management, password change, account recovery, ... - Ory Kratos: http://github.com/ory/kratos

- Permission management, roles, who is allowed to do what - Ory Keto: http://github.com/ory/keto

- OAuth2, OpenID Connect Provider that you "connect" to your user management (e.g. Ory Kratos) - Ory Hydra: http://github.com/ory/hydra

- A "middleware" which checks if requests are authenticated (who is the caller?) and authorized (is the caller allowed to do that) - Ory Oathkeeper: http://github.com/ory/oathkeeper

It's a bit like lego where the other projects are more like the full car you buy. The car might use little fuel but it's slow and you can't change that. The lego parts you can combine any way you want.

Plus, Ory is written in Go and we aim for supporting planet-scale distributed data stores to support global deployments with low latency, and other cool stuff!

The last point, we are actually building out a cloud service (think CockroachCloud without the licensing issues), which means that you don't buy a support contract from IBM but instead get everything with a few clicks! Kinda like Auth0, Okta, or Firebase - but with everything open source (maybe like sentry.io?)



	
	
ralala on Jan 13, 2021 | parent | next [–]


Thank you for the explanations and your hard work!

How stable is Ory? How often will breaking changes occur during the next months/years? Can you provide an ETA for the cloud service?



	
	
_hackerman on Jan 13, 2021 | root | parent | next [–]


Any time! You can learn more about software maturity here: https://www.ory.sh/docs/ecosystem/versioning

So basically Ory Hydra is the most stable and we did not have any big breaking changes (maybe a CLI command arg renamed) in the last 2 years iirc.

Cloud service is planned for a private beta in Q1 2021 (lmk if you are interested). Public release probably end of 2021 I think!



	
	
rad_gruchalski on Jan 13, 2021 | prev | next [–]


Keycloak is much heavier than Hydra. With Hydra, it is much easier to spin up thin OpenID clients. If one has a need to spin up dozens or hundreds of OpenID clients, Hydra will be definitely a better choice purely because one can have multiple Hydra servers running with only a handful of clients each. Think multi tenant environments. With Hydra, there is no reason not to have many Hydra instances with as low as a single OpenID client.

Hydra API is smaller and easier to use than the one from Keycloak. Because of how lightweight Hydra is, it is possible to spin it up in integration tests with docker using something like Ory dockertest.

What the Ory stack is missing is an implemetation of UMA2 and there is no out of the box support for LDAP auth and SAML federation. However, the way Hydra handles accepting an identity from an external authentication source via its admin API makes it fairly easy to add any auth mechanism, not limited to how it would be in Keycloak because of the Keycloak SPI design choices. Implementing the user federation SPI for Keycloak is actually pretty tricky.

What speaks for Keycloak is the completness: user and role management, permissions, resource servers and so on. However, if one wants just tokens and does not mind writing the glue code to Kratos and Keto, Ory stack is awesome. There is Oathkeeper serving as that glue layer and a sort of reverse proxy to all 3 of the components but it doesn’t always fulfil all requirements.



	
	
snuxoll on Jan 14, 2021 | parent | next [–]


Keycloak supports multi-tenancy natively with realms. There is a fixed memory cost for each, but it’s not like you have to spin up an entirely new instance for each.

I will agree that the SPI interfaces for Keycloak could be better, but especially with the new Quarkus distribution it’s stupidly easy to setup and has 99% of what you need out of the box.



	
	
rad_gruchalski on Jan 14, 2021 | root | parent | next [–]


> Keycloak supports multi-tenancy natively with realms. There is a fixed memory cost for each, but it’s not like you have to spin up an entirely new instance for each.

Yes, I know. I use Keycloak in production. All realms sit on one instance. As do all clients. It can get really heavy and really slow really fast, especially with resource servers. I am aware of replication but that is basically replicating the whole instance.

The other not so nice thing about the SPI is that custom providers are loaded into the main Java process and that comes with all the pitfalls of class loading, shading, uber jars. It’s a mess. Try building a log adapter to push data to Kafka or over grpc. Dragons.

Keycloak is nice for out of the box stuff but integration can get pretty messy.



	
	
gen220 on Jan 13, 2021 | prev [–]


We've been using Hydra as part of our single-sign-on stack for almost 3 years now. It's something that most application developers have no idea exists. I'd say it's been very successful.

We didn't use the other Ory offerings, instead opting to create our own user management and permissions suite. We already had LDAP as a competing source of truth, so this colored the picture. In 2021, I'd probably advocate for buying all-in to Ory tools.

If you're a shop that employs capable engineers, Ory is a strong recommendation. If you want something with a wide product surface area, you might want to look elsewhere.

To make a doubtlessly crude analogy, Hydra is kind of like the Kubernetes to the other options' OpenShift.







Guidelines | FAQ | Lists | API | Security | Legal | Apply to YC | Contact


Search:

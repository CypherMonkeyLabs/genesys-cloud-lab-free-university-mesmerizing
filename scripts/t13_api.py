from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "api",
    "title": "Platform APIs",
    "kicker": "No live calls",
    "accent": 1,
    "summary": "OAuth grants, client credentials limits, region hosts, and why this lab’s explorer never sends a request.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "p-center", "The Developer Center is the map. This lab is not a client.", "Core", 11,
    "It is the front door for the Platform API. Read the public docs. Do not point a tutorial at a production org.",
    [
        "The Genesys Cloud Developer Center is the front door for the Platform API. The API explorer in this lab shows sample JSON shaped from the client-credentials guide and from admin limits such as queue alerting. It does not call login or API hosts. A sample with labIllustration set to true is a teaching body, not a captured response.",
        "When you do build a client, the region’s login host and API host must match the organization. This lab treats only the US East API host from the client-credentials guide, api.mypurecloud.com, as a host it is willing to print. Other regions: confirm the API host on the regions article.",
    ],
    cites("dev", "cc-grant", "regions"),
    fig("Docs and samples stay on this side of the network.", [
        ("lab", "Lab", "architect", 18, 40),
        ("doc", "Dev Center", "region", 50, 40),
        ("org", "Org", "queue", 84, 40),
    ], [("lab", "doc"), ("doc", "org")]),
    "Decide whether a sample is safe to send",
    [
        ("Read", "Guide", "Client credentials page", "See the real request shape.", "Basic auth, not a secret in a query"),
        ("Lab", "Sample", "labIllustration", "Not a captured body.", "Do not file it as a bug"),
        ("Region", "Host", "Match the org", "US East API host is the one this lab prints.", "Confirm the others"),
        ("Prod", "Never", "Tutorial traffic", "Use a lab org.", "This site will not be your client"),
    ],
    [
        q("This lab’s API explorer:", "Shows samples and does not send them", ["Posts to your org", "Stores client secrets", "Replaces the Developer Center"], "It is a reader."),
        q("A body marked labIllustration is:", "A teaching sample, not a captured response", ["A production error you must reproduce", "An RFC", "A token"], "Do not treat it as a wire capture."),
        q("The Developer Center is:", "The public API map", ["An Edge group", "A queue", "A cert voucher"], "Start there."),
        q("The only API host this lab prints as documented is:", "api.mypurecloud.com", ["A guessed US West API host", "A private IP", "The PSAP"], "Other API hosts are confirmed on the regions article."),
        q("Client secrets belong:", "In a server-side secret store, never in this lab’s UI", ["In participant data", "In a flow name", "In a quiz"], "The guide uses a Basic header."),
        q("Tutorial requests belong in:", "A lab organization", ["The busiest production queue", "A secure payment flow", "An emergency route"], "Do not test on customers."),
    ],
    [("Explorer", "Does not send."), ("Illustration", "Not a capture."), ("Host", "Only US East is printed here."), ("Secret", "Never in the browser sample.")],
    "Mark three samples",
    ["One you would send from a lab org.", "One you would only read.", "The host you still need to confirm.", "Where the secret will live."],
    "The secret is not in the browser.",
    ("Secret in a ticket", "A client id and secret are pasted into a chat so a partner can “try the API”.", "The paste includes the Basic header.", "The secret left the server.", "Rotate the client. Use a lab org and a secret store."),
))

add(lesson(
    "p-grants", "Pick the grant that matches who the call runs as", "Core", 12,
    "Client credentials, authorization code with PKCE, and SAML2 Bearer are the grants to learn. Implicit is the one leaving.",
    [
        "The create-an-OAuth-client article lists the grant types you can assign. Client credentials are for a service. Authorization code, with PKCE where the article requires it, is for an application that acts as a user. SAML2 Bearer is the enterprise single-sign-on pattern the article includes. Token Implicit Grant is documented as deprecated after 25 May 2026.",
        "A grant is not a role. After you pick the grant you still assign role and division pairs. A correct grant with an empty role list returns a token that cannot see the queues you meant.",
    ],
    cites("oauth", "cc-grant"),
    fig("Grant first, then roles and divisions.", [
        ("g", "Grant", "architect", 16, 40),
        ("r", "Role", "wem", 48, 40),
        ("d", "Division", "region", 80, 40),
    ], [("g", "r"), ("r", "d")]),
    "Choose a grant out loud",
    [
        ("Service", "No user", "Client credentials", "Data actions and back-end jobs.", "Cannot call users/me"),
        ("User app", "A person", "Authorization code", "PKCE when the article says so.", "The token is that user"),
        ("SSO", "Enterprise IdP", "SAML2 Bearer", "As the article describes.", "Still needs roles"),
        ("Old", "Implicit", "Do not start here", "Deprecated after 25 May 2026.", "Migrate"),
    ],
    [
        q("A nightly job that is not a person should use:", "Client credentials", ["Implicit grant", "A password in the flow", "No OAuth"], "The guide is written for that case."),
        q("An app that must act as the signed-in user should use:", "Authorization code", ["Client credentials", "A queue name", "Bullseye"], "users/me needs a user."),
        q("SAML2 Bearer is:", "The enterprise SSO grant the OAuth article includes", ["A SIP method", "A number plan", "A bot type"], "Use it when the IdP is the point."),
        q("Token Implicit Grant is documented as:", "Deprecated after 25 May 2026", ["The only modern grant", "Required for SCIM", "Removed in 2019"], "Do not start a new app on it."),
        q("A token with no roles:", "Authenticates and still cannot do the work", ["Is an admin", "Bypasses divisions", "Publishes flows"], "Assign role and division pairs."),
        q("PKCE belongs with:", "Authorization code, when the article requires it", ["Client credentials Basic auth", "RTP", "ACW"], "Read the OAuth article rather than skipping PKCE."),
    ],
    [("Service", "Client credentials."), ("User", "Authorization code."), ("SSO", "SAML2 Bearer."), ("Implicit", "Deprecated after 25 May 2026.")],
    "Match four apps",
    ["A data action.", "A agent-desktop widget.", "An SSO portal.", "A legacy implicit app you would migrate."],
    "Each app has a different grant.",
    ("Password in a flow", "A data action stores a user’s password to call the API.", "No OAuth client. A secret in the action.", "The grant was skipped.", "Create a client-credentials client and delete the password."),
))

add(lesson(
    "p-cc", "Client credentials have no user, so users/me is the wrong call", "Core", 12,
    "The token is the client. The guide shows that limit on purpose.",
    [
        "The client-credentials guide shows a POST to the login host’s /oauth/token with HTTP Basic of the client id and secret, and grant_type=client_credentials. The access token is then a bearer token against the API host. The same guide explains that this token cannot call /api/v2/users/me, because there is no user.",
        "Roles on a client-credentials client are role-and-division pairs, and they are a subset of what the person who created the client could grant. You cannot escalate by creating a client. If the integration must read “my” queues, use authorization code instead.",
    ],
    cites("cc-grant", "oauth"),
    fig("Basic auth at login. Bearer at the API. No user on the token.", [
        ("id", "Client", "architect", 14, 40),
        ("login", "Login host", "region", 46, 40),
        ("api", "API host", "queue", 78, 40),
    ], [("id", "login"), ("login", "api")]),
    "Read a token request without sending it",
    [
        ("POST", "/oauth/token", "grant_type=client_credentials", "On the login host.", "Basic, not the secret in the body if the guide uses the header"),
        ("Response", "access_token", "Bearer", "expires_in comes from the response.", "Do not hardcode a lifetime"),
        ("GET", "/api/v2/users", "A call the guide shows", "Against the API host.", "US East sample: api.mypurecloud.com"),
        ("GET", "/api/v2/users/me", "Do not", "No user context.", "Switch grants if you need it"),
    ],
    [
        q("Client credentials are sent as:", "HTTP Basic of client id and secret, plus grant_type=client_credentials", ["A password grant in Architect", "A SIP REGISTER", "A queue id"], "Follow the guide."),
        q("/api/v2/users/me with that token:", "Fails because the token is not a user", ["Returns the admin who created the client", "Lists all divisions", "Is the happy path"], "The guide documents the limit."),
        q("The bearer token is used against:", "The API host for the org’s region", ["The Edge", "The carrier", "The PSAP"], "Login and API hosts are different."),
        q("expires_in should be:", "Read from the token response", ["Assumed to be one year", "Ignored", "Stored in a flow name"], "Refresh on the documented schedule."),
        q("A client-credentials role can exceed the creator’s rights:", "No. Pairs are a subset of what the creator could grant.", ["Yes", "Only in Home", "Only for SCIM"], "You cannot escalate through a client."),
        q("Listing users, as in the guide’s example, is:", "A normal client-credentials call when the role allows it", ["The same as users/me", "Forbidden always", "A bot flow"], "The absence of a user is not the absence of all user APIs."),
    ],
    [("Basic", "Id and secret at the login host."), ("Bearer", "The API host."), ("users/me", "Wrong grant."), ("Subset", "No privilege escalation.")],
    "Explain the 403 illustration",
    ["Which grant you used.", "Which path failed.", "Which grant you would switch to.", "Where the secret is stored."],
    "The explanation does not include the secret.",
    ("Me with a bot", "A service account’s health check calls /users/me and pages on 403.", "Grant: client credentials.", "The health check expects a user.", "Check /api/v2/users or a resource the role allows, or switch grants."),
))

add(lesson(
    "p-implicit", "Implicit grant is a migration, not a new design", "Core", 11,
    "The OAuth article dates the deprecation: after 25 May 2026.",
    [
        "Token Implicit Grant returns a token in the browser redirect. That pattern is what the create-an-OAuth-client article marks deprecated after 25 May 2026. New work uses authorization code with PKCE, or client credentials when there is no user. Leaving an implicit client in place is a dated risk, not a style choice.",
        "Inventory the clients before the date. Each one is either a user-facing app or a service. Split them. Do not “fix” an implicit app by pasting its token into a data action.",
    ],
    cites("oauth", "cc-grant"),
    fig("Implicit clients move to code+PKCE or to client credentials.", [
        ("old", "Implicit", "crm", 16, 40),
        ("code", "Code + PKCE", "architect", 55, 22),
        ("cc", "Client credentials", "region", 55, 68),
    ], [("old", "code"), ("old", "cc")]),
    "Inventory and split",
    [
        ("Admin", "List", "Every OAuth client", "Grant column.", "Including ones partners created"),
        ("User app", "Move", "Authorization code", "Add PKCE.", "Test in a lab org"),
        ("Service", "Move", "Client credentials", "Roles and divisions only.", "No users/me"),
        ("Date", "25 May 2026", "The article’s line", "Re-read in case the page moves.", "Do not invent an earlier kill date"),
    ],
    [
        q("Token Implicit Grant is deprecated after:", "25 May 2026, on the OAuth client article", ["1 January 2020", "The next Edge upgrade", "Never"], "Use the article’s date."),
        q("A new single-page app that acts as a user should use:", "Authorization code with PKCE", ["Implicit", "A password in localStorage", "Client credentials for users/me"], "That is the replacement."),
        q("A service mistaken for a user app should use:", "Client credentials, and stop calling users/me", ["Implicit forever", "SAML inside a trunk", "No auth"], "Split the inventory."),
        q("Pasting an implicit token into a data action:", "Does not modernize the client", ["Is the migration", "Rotates the secret", "Publishes flows"], "Change the grant."),
        q("The deprecation date in a design packet should be:", "Copied from the current article", ["Remembered from this lesson if the page changed", "Omitted", "Set to a community rumor"], "Re-read before you enforce it."),
        q("Partners’ OAuth clients are:", "In the same inventory", ["Exempt", "Cisco objects", "Number plans"], "You own the org’s clients."),
    ],
    [("Date", "25 May 2026 on the article."), ("User", "Code and PKCE."), ("Service", "Client credentials."), ("Inventory", "Including partners.")],
    "Classify five imaginary clients",
    ["Two user apps.", "Two services.", "One you cannot classify until you see the grant.", "The page you will re-open."],
    "Nothing stays implicit without a date.",
    ("Forgotten widget", "A browser widget still uses a hash token after the deprecation date.", "Grant: Token Implicit.", "The inventory skipped it.", "Move it to authorization code with PKCE."),
    "Confirm the deprecation sentence on the OAuth article before you enforce 25 May 2026 in a program plan.",
))

add(lesson(
    "p-hosts", "Login host and API host are a pair you look up", "Core", 12,
    "US East is the pair this lab will quote in full. Other rows stay on the regions article.",
    [
        "US East (N. Virginia, us-east-1) uses login.mypurecloud.com and, in the client-credentials guide, api.mypurecloud.com. US West (Oregon, us-west-2) uses login.usw2.pure.cloud. FedRAMP (US East 2, us-east-2) uses login.use2.us-gov-pure.cloud. This lab does not invent the API hostname that pairs with those last two logins.",
        "A token from one region’s login host is not a token for another region’s API. Satellite regions do not change this. They are media. The organization still has one core region and one login.",
    ],
    cites("regions", "cc-grant", "gcv-regions"),
    fig("One core region, one login, one API host.", [
        ("org", "Core org", "region", 20, 40),
        ("login", "Login", "architect", 52, 40),
        ("api", "API", "queue", 82, 40),
    ], [("org", "login"), ("login", "api")]),
    "Bind a client to the right pair",
    [
        ("Org", "Region", "Read the org’s region", "Not the user’s laptop.", "Core, not satellite"),
        ("US East", "Pair", "login.mypurecloud.com and api.mypurecloud.com", "The pair this lab quotes.", "Guide plus regions article"),
        ("US West", "Login", "login.usw2.pure.cloud", "API host: look it up.", "Do not guess api.usw2"),
        ("FedRAMP", "Login", "login.use2.us-gov-pure.cloud", "API host: look it up.", "Voice coverage is a different article"),
    ],
    [
        q("The US East login host is:", "login.mypurecloud.com", ["login.usw2.pure.cloud", "login.use2.us-gov-pure.cloud", "api.mypurecloud.com"], "The API host is the other name."),
        q("The US East API host shown in the client-credentials guide is:", "api.mypurecloud.com", ["login.mypurecloud.com", "A satellite region", "The Edge"], "Do not swap login and API."),
        q("US West’s login host is:", "login.usw2.pure.cloud", ["login.mypurecloud.com", "A host this lab invented for the API", "The carrier"], "The API pair is confirmed on the regions article."),
        q("A token from US East used against another region:", "Is the wrong pair", ["Is faster", "Is required for satellite media", "Publishes flows"], "Match the org."),
        q("A satellite region:", "Does not replace the org’s login host", ["Is where you create the org", "Issues OAuth clients", "Stores roles"], "Media is not the core."),
        q("FedRAMP’s login host is:", "login.use2.us-gov-pure.cloud", ["login.mypurecloud.com", "A commercial guess", "appfoundry.genesys.com"], "us-east-2 in the regions article."),
    ],
    [("US East", "login.mypurecloud.com / api.mypurecloud.com."), ("US West", "login.usw2.pure.cloud. Confirm the API host."), ("FedRAMP", "login.use2.us-gov-pure.cloud. Confirm the API host."), ("Satellite", "Not an org home.")],
    "Fill the pair",
    ["The org’s core region.", "The login host.", "The API host, or the words “confirm on the regions article”.", "A sentence that satellite media does not change the pair."],
    "No guessed API hostname remains.",
    ("West token, east API", "Every call returns unauthorized after a region migration on paper.", "Token from login.usw2.pure.cloud. Requests still go to api.mypurecloud.com.", "The pair was split.", "Point the client at the API host the regions article lists for that org."),
))

add(lesson(
    "p-roles", "Role and division pairs are the real permission", "Core", 12,
    "A token opens the door the role allows, in the division the pair names.",
    [
        "Divisions overview: objects live in one division, Home cannot be deleted, and the All division is the org-wide grant. OAuth clients do not escape that model. The client-credentials article’s role-division pairs are how a service is scoped. Granting a queue role in Home does not let the client edit a queue that lives in another division.",
        "Transactional objects such as conversations and recordings follow the division rules on that page. An integration that “cannot see the recording” is often a division grant, not a broken endpoint. Check the pair before you file an API defect.",
    ],
    cites("divisions", "oauth", "cc-grant"),
    fig("The same role in two divisions is two grants.", [
        ("role", "Queue edit", "wem", 22, 40),
        ("home", "Home", "region", 58, 22),
        ("emea", "EMEA", "region", 58, 68),
    ], [("role", "home"), ("role", "emea")]),
    "Scope a service to one division",
    [
        ("Need", "One business unit", "That division only", "Not All, unless you mean the org.", "All is a real grant"),
        ("Client", "Pairs", "Role plus division", "Subset of the creator.", "No escalation"),
        ("Test", "Other division", "Expect a miss", "That proves the scope.", "Do not “fix” it with All on a Friday"),
        ("Audit", "Who created it", "Their rights cap the client", "If they lose a division, review the client.", "Pairs do not grow on their own"),
    ],
    [
        q("A role granted only in Home lets the client:", "Work on objects in Home", ["Edit every division", "Delete Home", "Bypass OAuth"], "Division is part of the pair."),
        q("The All division is:", "An org-wide grant, used on purpose", ["A default you should always add", "The same as Home", "A satellite region"], "It is powerful."),
        q("Client-credentials pairs are limited by:", "What the creator could grant", ["The carrier", "The bot", "The exam"], "No escalation."),
        q("A recording the API “lost” is often:", "A division the token cannot see", ["A SIP 404", "An unpublished in-queue flow", "A 988 plan"], "Check the pair."),
        q("Home division:", "Cannot be deleted", ["Is optional", "Is a trunk", "Is implicit grant"], "The divisions article says so."),
        q("Two queues in two divisions need:", "Grants that cover both, if one client must edit both", ["One Home grant", "No roles", "A preferred agent"], "Objects have one division each."),
    ],
    [("Pair", "Role plus division."), ("All", "Org-wide, on purpose."), ("Home", "Cannot be deleted."), ("Creator", "Caps the client.")],
    "Write the pairs",
    ["The client name.", "The role.", "The division.", "The division you expect to fail a test call."],
    "The failure is intentional.",
    ("All by habit", "A partner integration can edit every queue in the org.", "Role pair: All division.", "The scope was the whole org.", "Replace All with the division that owns those queues."),
))

add(lesson(
    "p-scim", "SCIM and other directory sync still start with an OAuth client", "Core", 11,
    "The OAuth article points SCIM at a client. The client still has roles and a grant.",
    [
        "Create an OAuth client is the article that tells you SCIM uses an OAuth client. Treat that client like any other service: a deliberate grant, least roles, a division pair, a secret that is not in a ticket. Directory sync that can create users can also create admins if the role is wide.",
        "SCIM does not choose your region, your queues, or your bots. After users exist, the org work in the other tracks still has to happen. A synced user with no queue membership and Off Queue is a successful SCIM call and an empty contact center.",
    ],
    cites("oauth", "divisions", "queues"),
    fig("Directory to OAuth client to a user who still needs a queue.", [
        ("dir", "Directory", "crm", 14, 40),
        ("oa", "OAuth", "architect", 46, 40),
        ("q", "Queue", "queue", 80, 40),
    ], [("dir", "oa"), ("oa", "q")]),
    "Stand up sync without standing up admins",
    [
        ("Admin", "Client", "Its own OAuth client", "Not a person’s implicit token.", "Client credentials or the grant the article names"),
        ("Admin", "Roles", "Only user provision", "Not every permission the creator has.", "Division pairs"),
        ("Secret", "Store", "A vault", "Rotate if it leaks.", "Never in this lab"),
        ("After", "Queues", "Membership is separate", "SCIM did not join them to Billing.", "On Queue is still a status"),
    ],
    [
        q("SCIM in Genesys Cloud is tied to:", "An OAuth client, per the OAuth article", ["A phone trunk", "An in-queue flow", "A cert voucher"], "Start there."),
        q("A wide SCIM role can:", "Provision more access than you meant, including privileged users", ["Only set ACW", "Only buy numbers", "Only read the FAQ"], "Least privilege."),
        q("A synced user who never takes a call often:", "Has no queue membership or is not On Queue", ["Needs a new region", "Needs implicit grant", "Needs a topic"], "SCIM creates the person, not the contact center."),
        q("The client secret for SCIM belongs in:", "A secret store", ["A flow name", "Participant data", "A quiz answer"], "Rotate it if it escapes."),
        q("Division pairs still apply because:", "The client is an OAuth client", ["SCIM bypasses divisions", "Home was deleted", "Tokens are queues"], "Scope the directory client."),
        q("After a successful sync you still configure:", "Queues, roles, and presence behavior", ["Only the trunk", "Only the exam", "Nothing"], "The user is not yet an agent."),
    ],
    [("Client", "Its own OAuth client."), ("Roles", "Provision, not everything."), ("Secret", "A vault."), ("After", "Queues and On Queue.")],
    "Review a SCIM client",
    ["The grant.", "The roles.", "The divisions.", "One thing SCIM will not configure for you."],
    "The last item is queue membership or presence.",
    ("Admin sync", "Every new hire is an organization admin.", "SCIM role includes admin permissions.", "The pair was copied from the project owner.", "Replace it with a provision-only role and review who was created."),
))

from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "crm",
    "title": "AppFoundry and CRM",
    "kicker": "Beside the desktop",
    "accent": 2,
    "summary": "The marketplace, the documented Salesforce and Zendesk embeds, and OAuth migrations that do not invent other CRMs.",
    "lessons": [],
}


def add(item):
    TRACK["lessons"].append(item)


add(lesson(
    "i-market", "AppFoundry is the marketplace, not a feature you assume is installed", "Core", 11,
    "An app is present only after someone installs it into the org.",
    [
        "AppFoundry is Genesys’ marketplace for applications that extend Genesys Cloud. The site is the catalog. An org does not gain screen pop, a workforce add-on, or a bot connector because the listing exists. Someone with the right admin rights installs it, and that install often creates an OAuth client.",
        "This lab cites the marketplace and the product articles it can open. If a CRM is not Salesforce or Zendesk in those articles, the lesson will say “look on AppFoundry” rather than invent a feature list. Listings change. Re-open the listing before you write it into a design.",
    ],
    cites("appfoundry", "oauth", "dev"),
    fig("A listing becomes an install, which becomes an OAuth client.", [
        ("list", "Listing", "crm", 16, 40),
        ("org", "Org", "region", 48, 40),
        ("oa", "Client", "architect", 80, 40),
    ], [("list", "org"), ("org", "oa")]),
    "Treat a listing as a candidate",
    [
        ("Read", "Listing", "What it claims today", "Not a screenshot from last year.", "AppFoundry"),
        ("Admin", "Install", "Into this org", "Permissions required.", "Often an OAuth client"),
        ("Scope", "Division", "Role pairs", "The client is not All unless you say so.", "Divisions still apply"),
        ("Other CRM", "No article", "Do not invent", "Point at the marketplace.", "Salesforce and Zendesk have product pages"),
    ],
    [
        q("AppFoundry is:", "The marketplace of apps you can install", ["A core AWS region", "A queue type", "An exam"], "The org is unchanged until you install."),
        q("A listing by itself:", "Does not configure your org", ["Creates queues", "Buys numbers", "Passes GC-GCP"], "Install is a step."),
        q("Installs often create:", "An OAuth client you must scope", ["A premises Edge", "A PSAP", "A cert voucher"], "Treat it like any other client."),
        q("A CRM this lab has not opened a product article for:", "Is “check AppFoundry”, not a feature list", ["Is identical to Salesforce", "Is unsupported forever", "Is UCCE"], "Do not invent."),
        q("Listings change, so a design should:", "Link the live listing", ["Freeze a 2023 screenshot as the contract", "Ignore permissions", "Use implicit grant"], "Re-open it."),
        q("The Developer Center relates because:", "Custom apps and OAuth still follow the platform rules", ["It replaces AppFoundry", "It is a trunk", "It is WFM"], "Marketplace apps are still API clients."),
    ],
    [("Listing", "A candidate."), ("Install", "The moment it exists."), ("Client", "Scope it."), ("Unknown CRM", "Marketplace, not fiction.")],
    "Review one listing",
    ["The name.", "The permission it asks for.", "The division you would grant.", "What you will not claim if the listing is vague."],
    "The vague claim is left out.",
    ("Assumed install", "The design says screen pop works. The org has no app installed.", "AppFoundry listing bookmarked. OAuth clients: none for that app.", "The bookmark was treated as an install.", "Install it, or remove it from the design."),
))

add(lesson(
    "i-sf", "Genesys Cloud for Salesforce is a documented embed", "Core", 12,
    "Screen pop, click-to-dial, logging, and the assist features that page names.",
    [
        "The About Genesys Cloud for Salesforce article describes the embed: agents work in Salesforce with Genesys capabilities such as screen pop, click-to-dial, and interaction logging. The page also discusses Agent Assist and Agent Copilot in that embed. Those sentences are the feature list this lab will repeat. Anything the page does not say, including a field map for your objects, is your design work.",
        "The embed is not the Salesforce OAuth client-credentials migration. Logging a call and calling a Salesforce API from a data action are two integrations. They can share a vocabulary and still use different credentials. Configure both on purpose.",
    ],
    cites("salesforce", "copilot", "sf-oauth"),
    fig("The embed is the desktop. A data action is a different credential.", [
        ("sf", "Salesforce", "crm", 16, 40),
        ("emb", "Embed", "agent", 48, 22),
        ("da", "Data action", "architect", 48, 68),
    ], [("sf", "emb"), ("sf", "da")]),
    "Separate the two Salesforce paths",
    [
        ("Desktop", "Embed", "Screen pop and click-to-dial", "The about article.", "Logging too"),
        ("Assist", "Copilot", "Only as that page describes", "Do not add features.", "CX 4 still governs Copilot’s package story"),
        ("Flow", "Data action", "Its own OAuth", "The migration guide.", "Not the agent’s password"),
        ("Map", "Your objects", "Not in this lab", "Write the field map yourselves.", "The article will not know your schema"),
    ],
    [
        q("Genesys Cloud for Salesforce, per its article, includes:", "Screen pop, click-to-dial, and logging", ["BYOC trunks", "Edge groups", "Bullseye rings"], "Those are the embed’s job."),
        q("Agent Assist and Copilot in that article are:", "Mentioned on the Salesforce page, and still subject to the Copilot overview", ["A replacement for ACD", "Free on CX 1", "SIP methods"], "Read both pages."),
        q("A data action into Salesforce is:", "A separate integration from the embed", ["The same toggle", "A number plan", "A queue member"], "Give it its own OAuth."),
        q("Your custom object map is:", "Your design. The article does not know it.", ["Published as an RFC", "Fixed by Home division", "A default number plan"], "Write it down."),
        q("Putting an agent password in a data action:", "Is the pattern the migration guide tells you to leave", ["Is required", "Is PKCE", "Is SCIM"], "Use the OAuth client credentials flow."),
        q("The embed fails open to a full contact center when:", "It does not. Queues and flows still exist in Genesys.", ["Always", "On CX 2", "If click-to-dial works"], "CRM is beside ACD, not instead of it."),
    ],
    [("Embed", "Pop, dial, log."), ("Assist", "As the page states."), ("Data action", "Separate OAuth."), ("Schema", "Yours to map.")],
    "List the embed and the action",
    ["Three embed features you can cite.", "Whether Copilot is in scope.", "The data action’s grant.", "One field you will not pretend the article mapped."],
    "The unmapped field is explicit.",
    ("One password", "The data action still uses a Salesforce username and password after the embed was installed.", "Embed: installed. Action: password grant.", "The embed did not migrate the action.", "Follow the OAuth client-credentials migration guide."),
))

add(lesson(
    "i-sf-oauth", "Salesforce data actions move to OAuth client credentials", "Core", 12,
    "Consumer key, secret, and My Domain URL. The request body of the action stays.",
    [
        "The Salesforce OAuth client-credentials migration guide describes leaving username-password auth. You create a Salesforce OAuth client, and you give Genesys the consumer key, the secret, and the My Domain URL. The guide says the data action’s request body does not have to change for that migration. Read the guide for the clicks. This lesson is the shape, not a second copy of the clicks.",
        "A different article, configure OAuth settings, covers CX Cloud from Genesys and Salesforce OAuth settings. Do not mix that page with the data-action migration and call them one wizard. Two pages, two jobs.",
    ],
    cites("sf-oauth", "sf-settings", "salesforce"),
    fig("Password auth leaves. Client credentials stay. The action body stays.", [
        ("pw", "Password", "crm", 14, 40),
        ("cc", "OAuth client", "architect", 48, 40),
        ("body", "Same body", "wem", 82, 40),
    ], [("pw", "cc"), ("cc", "body")]),
    "Migrate the credential, not the JSON",
    [
        ("SF", "Client", "OAuth client credentials", "In Salesforce.", "Consumer key and secret"),
        ("GC", "Action", "My Domain URL", "The guide’s inputs.", "Plus the secret in a real store"),
        ("Body", "Unchanged", "The request you already tested", "The guide’s point.", "Still re-test"),
        ("Other", "CX Cloud page", "A different article", "Do not skip it if you use that product.", "Do not confuse it with this one"),
    ],
    [
        q("The migration guide replaces:", "Username-password auth on the Salesforce data action", ["The Architect flow", "The queue", "The region"], "The credential changes."),
        q("Genesys needs:", "Consumer key, secret, and My Domain URL", ["The agent’s laptop password", "An Edge serial", "A topic phrase"], "Those are the guide’s inputs."),
        q("The data action request body:", "Can stay, per the guide", ["Must be rewritten as SIP", "Is deleted", "Becomes a bot"], "Re-test anyway."),
        q("Configure OAuth settings is:", "A separate article from the data-action migration", ["The same page", "A number plan", "An exam"], "CX Cloud settings live there."),
        q("The secret in a shared document is:", "A leak. Rotate it.", ["The My Domain", "Required by the lab", "A division"], "Store it as a secret."),
        q("After migration, a failure to pop the Salesforce record:", "May be the embed, not the data action", ["Is always the consumer key", "Is bullseye", "Is ACW"], "They are different paths."),
    ],
    [("Leave", "Username and password."), ("Bring", "Key, secret, My Domain."), ("Keep", "The action body, then re-test."), ("Other page", "CX Cloud OAuth settings.")],
    "Write the cutover",
    ["The old auth.", "The three new inputs.", "What you will re-test.", "Which article is not this migration."],
    "The other article is named.",
    ("Half migrated", "Flows fail on Monday. The password was disabled in Salesforce and the action was not updated.", "Salesforce: password login off. Genesys action: still password.", "The cutover was one-sided.", "Apply the client-credentials inputs and re-test the action."),
))

add(lesson(
    "i-zd", "Zendesk has its own about page, with a similar embed idea", "Core", 11,
    "Do not copy the Salesforce field list onto Zendesk.",
    [
        "About Genesys Cloud for Zendesk documents an embed in the same family: agents handle Genesys interactions from Zendesk, with the screen-pop and productivity features that page describes. Read that page for the list. This lab will not paste unverified feature parity.",
        "OAuth still applies. A Zendesk app that calls the Platform API is a client with a grant and roles. The Salesforce migration guide is not the Zendesk guide. If you need a Zendesk credential change, open the Zendesk article rather than reusing the My Domain steps.",
    ],
    cites("zendesk", "oauth", "salesforce"),
    fig("Zendesk is its own article beside Salesforce.", [
        ("zd", "Zendesk", "crm", 22, 40),
        ("gc", "Genesys", "region", 55, 40),
        ("sf", "Salesforce", "crm", 84, 70),
    ], [("zd", "gc"), ("sf", "gc")]),
    "Cite the page you mean",
    [
        ("Design", "Zendesk", "Open the Zendesk about article", "Write only what it says.", "No parity assumptions"),
        ("Design", "Salesforce", "Leave it in the other lesson", "My Domain is not a Zendesk field.", "Different guide"),
        ("API", "Client", "Grant and roles", "If the app calls Genesys.", "Divisions included"),
        ("Unknown", "Feature", "Mark it unconfirmed", "Or cut it.", "The uncertainty line exists for this"),
    ],
    [
        q("Zendesk’s feature list should come from:", "The Zendesk about article", ["The Salesforce article", "A UCCE guide", "Memory"], "They are different pages."),
        q("My Domain URL is:", "A Salesforce migration input, not a Zendesk step", ["Required on every CRM", "A login host", "A queue"], "Do not reuse it blindly."),
        q("An app in Zendesk that calls Genesys is:", "An OAuth client", ["A phone trunk", "A topic", "A cert"], "Scope the roles."),
        q("Screen pop on Zendesk is:", "Whatever the Zendesk article describes", ["Guaranteed identical to Salesforce", "A bullseye ring", "An Edge group"], "Read the page."),
        q("Inventing parity is:", "How designs fail acceptance", ["Required", "Fair use", "Preferred routing"], "Mark gaps."),
        q("Both embeds still leave you to build:", "Queues, flows, and hours in Genesys", ["Nothing", "A new core region", "An implicit grant"], "CRM does not replace Architect."),
    ],
    [("Source", "The Zendesk article."), ("Not", "The Salesforce My Domain steps."), ("Client", "If it calls the API."), ("Gap", "Say unconfirmed.")],
    "Two columns",
    ["Three items you will only claim for Salesforce.", "Three you will only claim after reading Zendesk.", "One shared rule: OAuth.", "One shared rule: Genesys still owns the queue."],
    "The columns are not copies.",
    ("Copied map", "Zendesk screen pop looks up a Salesforce field that does not exist.", "Design table pasted from the Salesforce workshop.", "The CRM was swapped without the article.", "Rewrite the row from the Zendesk page."),
))

add(lesson(
    "i-other", "Dynamics, ServiceNow, and the rest stay on the marketplace", "Core", 11,
    "No invented feature lists for CRMs this lab did not open.",
    [
        "People will ask for Microsoft Dynamics and ServiceNow in the same breath as Salesforce. This lab did not confirm a product article for those embeds while it was written. The honest answer is AppFoundry plus the Developer Center: find the listing, read it, and if you build your own, use OAuth and data actions under the rules you already have.",
        "A custom CRM integration is a client and a set of data actions, not a new routing method. The conversation still queues in Genesys. The CRM stores the record. When the data action times out, the agent still has the call. Draw that failure in Architect.",
    ],
    cites("appfoundry", "dev", "oauth", "architect"),
    fig("Unknown CRM: listing or a client you build. The queue remains.", [
        ("m", "Marketplace", "crm", 16, 28),
        ("c", "Your client", "architect", 48, 28),
        ("q", "Queue", "queue", 80, 60),
    ], [("m", "q"), ("c", "q")]),
    "Answer the Dynamics question without fiction",
    [
        ("Ask", "Listing", "Open AppFoundry", "Read what is there today.", "Do not quote this lab"),
        ("Build", "OAuth", "A client", "Grant, roles, divisions.", "Secret in a vault"),
        ("Flow", "Data action", "Timeout path", "The call continues.", "Do not strand the caller on a CRM"),
        ("Write", "Uncertainty", "What you did not confirm", "Put it in the design.", "Better than a fake feature"),
    ],
    [
        q("This lab’s feature list for Dynamics is:", "None. Confirm a listing or an article.", ["Identical to Salesforce", "Identical to UCCE", "A default number plan"], "Honesty is the feature."),
        q("A homegrown CRM integration is:", "An OAuth client and data actions", ["A new ACD method", "An Edge model", "A specialist exam"], "Routing does not move."),
        q("When the CRM times out:", "The conversation should still be handled in Genesys", ["The caller is dropped by design", "Bullseye deletes the queue", "Implicit grant refreshes it"], "Draw the failure."),
        q("ServiceNow in a statement of work should cite:", "A listing or article you opened", ["This lesson’s imagination", "RFC 3550", "The STA dialect table"], "This lesson refuses the list."),
        q("AppFoundry plus the Developer Center is:", "The pair of doors for an unknown system", ["A region pair", "A bot type", "A cert"], "Listing or custom client."),
        q("Divisions apply to a custom client because:", "It is still an OAuth client", ["Only Salesforce is divided", "Home was removed", "SCIM is exempt"], "Scope the pairs."),
    ],
    [("Unknown", "No invented list."), ("Build", "OAuth and data actions."), ("Timeout", "The call continues."), ("Cite", "A page you opened.")],
    "Write the uncertainty",
    ["The CRM name.", "The sentence “not confirmed in this lab”.", "Where you will look.", "The Architect failure path."],
    "The failure path is a queue action, not a hope.",
    ("Invented pop", "The build promises ServiceNow screen pop with a field map nobody sourced.", "No listing and no article in the packet.", "The map was fiction.", "Cut the paragraph until a listing or a design you tested replaces it."),
    "This lab did not confirm Dynamics or ServiceNow product articles. Do not treat this page as one.",
))

add(lesson(
    "i-fail", "A CRM failure is not an ACD failure", "Core", 11,
    "Screen pop can die while the queue is healthy.",
    [
        "Agents describe a CRM outage as “Genesys is down” because the panel they look at is the CRM. The topology in this lab splits those links on purpose. Data-action timeouts and embed outages leave the conversation on the agent. Your Architect flow should not wait forever on a data action before it transfers to a queue.",
        "Client-credentials roles must include the division that owns the data action and the queue. A 403 that starts on Monday is often a division move on Friday. Check the pair before you rebuild the flow.",
    ],
    cites("architect", "divisions", "salesforce", "oauth"),
    fig("The CRM link can drop. The queue link should not.", [
        ("a", "Agent", "agent", 30, 40),
        ("c", "CRM", "crm", 70, 18),
        ("q", "Queue", "queue", 70, 70),
    ], [("a", "c"), ("a", "q")]),
    "Design the timeout",
    [
        ("Flow", "Data action", "A short timeout", "Then Transfer to ACD.", "Do not loop the action"),
        ("Agent", "Embed", "A manual search path", "If pop fails.", "The call is still there"),
        ("Admin", "403", "Check division pairs", "Did the queue move?", "Roles do not follow automatically"),
        ("Comms", "Status", "Say which system failed", "CRM versus Genesys.", "Stops the wrong bridge call"),
    ],
    [
        q("A data action timeout should:", "Fall through to the queue", ["Retry for the whole hold time", "Drop the caller", "Switch regions"], "The conversation is the priority."),
        q("Agents saying Genesys is down during a CRM outage:", "Need a status that names the CRM", ["Are always right", "Mean the Edge is offline", "Mean implicit grant expired"], "Split the links."),
        q("A 403 after a queue changes division is often:", "The OAuth pair still points at the old division", ["A codec mismatch", "A topic miss", "A 988 plan"], "Update the pair."),
        q("Screen pop and ACD are:", "Independent enough that one can fail alone", ["The same service", "Both number plans", "Both exams"], "Test them separately."),
        q("Looping a data action until it works:", "Traps the caller in the flow", ["Is bullseye", "Is preferred routing", "Is SCIM"], "Cap it and transfer."),
        q("The division that owns the data action must be:", "In the client’s role pairs", ["Home always", "All always", "Empty"], "Least privilege that still works."),
    ],
    [("Timeout", "Then queue."), ("Status", "Name the CRM."), ("403", "Check the division pair."), ("Pop", "Can fail while ACD works.")],
    "Write the failure sentence",
    ["How long the flow waits.", "Where it transfers.", "What the agent does if pop fails.", "Who updates OAuth pairs after a division move."],
    "A person is named for the pair update.",
    ("Infinite dip", "Callers sit in silence while a data action retries through a CRM outage.", "Timeout: none. Failure output: empty.", "The flow trusted the CRM.", "Add a timeout and Transfer to ACD."),
))

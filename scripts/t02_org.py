from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "org",
    "title": "Organization and licensing",
    "kicker": "Admin",
    "accent": 2,
    "summary": "Regions, roles, divisions, named and concurrent licenses, packages, and fair use.",
    "lessons": [],
}

def add(item):
    TRACK["lessons"].append(item)

add(lesson(
    "o-place", "Place the organization in a core region", "Core", 12,
    "You do not move an org between regions as a setting. You create it in a core region and live with that login host.",
    [
        "The regions article is explicit: the organization is deployed in a core region chosen from its location, and users sign in on that region’s URL. Satellite regions never become that home. If a runbook says “point the org at the satellite closest to the agents,” it has mixed media design with org identity.",
        "Genesys Cloud Voice is not available in every core region, and country coverage inside a region is restricted. The FedRAMP region’s voice article limits non-US country services. The European Sovereign region has its own boundary rules for where voice may be processed. Read those pages before you promise a number in a country.",
    ],
    cites("regions", "gcv-regions"),
    fig("Identity stays in the core. Media may use a satellite.", [
        ("login", "Login", "region", 20, 30),
        ("org", "Org data", "region", 48, 30),
        ("media", "Satellite", "trunk", 78, 60),
    ], [("login", "org"), ("org", "media")]),
    "Separate org home from media home",
    [
        ("Planner", "Regions", "Pick core", "The org is created in one core.", "Login URL is fixed to that row"),
        ("Planner", "GCV list", "Check voice", "Voice is only in some regions.", "Country table is separate"),
        ("Engineer", "Satellite", "Media only", "Use it to shorten audio, not to rehome the org.", "Recordings can sit there"),
        ("Security", "FedRAMP", "Different cloud", "use2.us-gov-pure.cloud is not the commercial host.", "Do not reuse a commercial token"),
    ],
    [
        q("What happens if you need the org in another core region?", "You are outside a simple setting change. The article describes creation in one core.", ["Toggle satellite to core", "Rename the Home division", "Publish the in-queue flow"], "Deployment region is chosen when the org is created."),
        q("A satellite region can store which of these, per the regions article?", "Media and recordings for Global Media Fabric", ["The organization’s only login", "OAuth client secrets as the org home", "WFM schedules as the org home"], "Satellites are media locations."),
        q("FedRAMP voice coverage in the Voice article is limited how?", "US numbers and US calling. Other countries are unavailable in that region.", ["Worldwide", "EU only", "No voice at all"], "The Voice restrictions article says other countries are unavailable in FedRAMP."),
        q("Which host is the commercial US East login?", "login.mypurecloud.com", ["login.use2.us-gov-pure.cloud", "login.usw2.pure.cloud", "appfoundry.genesys.com"], "That pairing is in the regions table."),
        q("European Sovereign voice processing outside the ESR boundary means:", "Those calls are not covered by the ESR data-sovereignty commitment", ["They are blocked", "They become BYOC automatically", "They are free"], "The Voice restrictions article says out-of-boundary calls use non-EU handling."),
        q("Global Media Fabric is configured from which object?", "The site", ["The OAuth client", "The evaluation form", "The fair use token"], "The regions article points at site configuration for Global Media Fabric."),
    ],
    [("Org home", "One core region and its login URL."), ("Satellite", "Media and recordings, not the org."), ("GCV", "Separate availability table."), ("FedRAMP", "A different login host and US-only voice.")],
    "Write the home region in the runbook",
    ["Record the AWS region name and the login URL.", "State whether Genesys Cloud Voice is offered there.", "State one country you will not promise until you read the country table.", "Say what a satellite is allowed to do."],
    "The runbook has a region row someone else can check.",
    ("Token from the wrong cloud", "A FedRAMP admin pastes a commercial client id into a gov runbook.", "Login host in the script: login.mypurecloud.com. Org: FedRAMP.", "The gov login host is login.use2.us-gov-pure.cloud.", "Replace the host with the FedRAMP row and issue the client in that org."),
    "The Voice article also lists planned or limited regions such as Mexico Central and the European Sovereign region. Treat “coming” and “limited” labels on that page as current only until you reload it.",
))

add(lesson(
    "o-roles", "Roles are permission lists paired with divisions", "Core", 13,
    "A role without a division grant does not open objects. An OAuth client inherits only a subset of its creator’s pairs.",
    [
        "Divisions overview is the access model: you grant a role on a division, and the user sees objects in that division. Queues, users, and flows are configuration objects you place. Conversations and recordings are transactional and pick up division context as they move.",
        "When you create a client-credentials OAuth client, you assign role and division pairs. The developer guide says those pairs are limited to a subset of what the creating user already has. A client cannot be used to escalate past its creator. It also cannot call /api/v2/users/me, because there is no user.",
    ],
    cites("divisions", "cc-grant", "oauth"),
    fig("A role meets a division. The client cannot outgrow its creator.", [
        ("user", "Admin", "agent", 16, 40),
        ("role", "Role", "wem", 42, 22),
        ("div", "Division", "queue", 42, 68),
        ("app", "OAuth client", "trunk", 78, 40),
    ], [("user", "role"), ("role", "div"), ("user", "app"), ("app", "div")]),
    "Grant the integration less than you have",
    [
        ("Admin", "Division", "Pick EMEA", "Objects in EMEA are the scope.", "Home is not automatic for every role"),
        ("Admin", "Role", "Pair them", "The grant is the pair, not the role alone.", "Queue stays invisible otherwise"),
        ("Admin", "OAuth", "Create client", "Choose Client Credentials for a service.", "Copy the secret once"),
        ("Admin", "Roles on client", "Subset", "You cannot assign a division you do not have.", "No privilege escalation"),
        ("App", "API", "Call /users", "A list call can work. /users/me will not.", "No user context"),
    ],
    [
        q("Client-credentials role assignments are limited by what?", "The role-division pairs of the user who creates the client", ["The fair use token count", "The number of queues", "The SIP codec"], "The developer guide states that limit."),
        q("Why does GET /api/v2/users/me fail for that grant?", "The token is not a user", ["The queue name has a space", "The Edge is offline", "Bullseye has six rings"], "The guide calls out user-context resources."),
        q("A supervisor who should see only one country needs:", "A role granted on that country’s division", ["The All-access password", "A second organization", "Architect publish rights only"], "Division grants are the access boundary."),
        q("Which grant does the OAuth article recommend for a Windows service?", "Client Credentials", ["Token Implicit", "A queue wrap-up code", "SAML for a browser user only"], "Client Credentials is the non-user grant. Implicit is documented as deprecated after 25 May 2026."),
        q("Transactional objects include:", "Conversations and recordings", ["Only trunk IPs", "Only prompt WAV files", "Only business units"], "The divisions article lists them."),
        q("Can the OAuth client be given a division the creator cannot see?", "No", ["Yes, if the secret is long", "Yes, on CX 1", "Only for Salesforce"], "Pairs are a subset of the creator’s access."),
    ],
    [("Pair", "Role plus division, not role alone."), ("Subset", "An OAuth client cannot exceed its creator."), ("/users/me", "Needs a user token."), ("Implicit", "Deprecated after 25 May 2026 in the OAuth article.")],
    "Design one integration grant",
    ["Name the division the integration must see.", "Name a role that can view queues in that division.", "State why /users/me is the wrong test call.", "Write down that the secret is shown once."],
    "You can review an OAuth client without giving it the whole org.",
    ("Over-broad client", "A billing integration can edit every division.", "Client roles: admin on All. Needed: read one queue.", "The creator assigned their own broad pair.", "Create a narrow role on the billing division and put only that pair on the client."),
))

add(lesson(
    "o-concurrent", "Named licenses and the concurrent peak", "Core", 12,
    "Concurrent billing charges the peak of simultaneous users, and it ignores peaks shorter than 30 minutes.",
    [
        "The concurrent licensing article says Genesys charges the maximum number of simultaneous users in the billing period, after discarding peaks shorter than 30 minutes. Peaks do not have to be one continuous block. The charge uses the highest Genesys Cloud CX license those users held during the period. The calculation stays inside one organization. It does not combine orgs.",
        "If you choose concurrent, the article says CX 1, CX 2, CX 3, and CX 4 users on that choice are licensed as concurrent. Named licensing is the other model: you assign a license to a person whether or not they are logged in. Fair use allocations also differ by named and concurrent user type, and the policy page is where those tables live.",
    ],
    cites("concurrent", "fair", "overview"),
    fig("A 20-minute spike does not set the concurrent bill. A 40-minute plateau does.", [
        ("spike", "20 min", "phone", 22, 30),
        ("peak", "40 min", "queue", 55, 30),
        ("bill", "Bill", "wem", 82, 30),
    ], [("peak", "bill")]),
    "Read a week of logins",
    [
        ("Org", "Model", "Concurrent", "All CX users in the model are concurrent.", "One org only"),
        ("Users", "Shift change", "Overlap 20 min", "Shorter than 30 minutes is discarded.", "Not the billed peak"),
        ("Users", "Overlap", "40 minutes", "This plateau can set the peak.", "Highest license level counts"),
        ("Finance", "Fair use", "Pool", "Allowances pool across users for the month.", "No rollover, per the policy summary"),
        ("Finance", "Second org", "Separate", "Concurrency is not shared across orgs.", "Do not add the peaks"),
    ],
    [
        q("How long must a concurrent peak last to count?", "Longer than 30 minutes", ["Longer than 30 seconds", "A full month", "It always counts"], "The article disregards peaks shorter than 30 minutes."),
        q("Two organizations can share one concurrent pool?", "No. The calculation is per organization.", ["Yes", "Only for CX 4", "Only in satellite regions"], "The article says concurrency is not calculated across orgs."),
        q("Which license level is billed when a user changes packages mid-period?", "The highest level assigned during the period", ["The lowest", "The one at midnight", "Always CX 1"], "The article bills the highest level assigned."),
        q("Named licensing differs because:", "The person consumes a license even when logged out", ["It ignores CX 4", "It is illegal", "It is only for trunks"], "Named assigns the license to the user rather than to a simultaneous peak."),
        q("Fair use allocations, as described on the policy page, do what at month end?", "They pool across users and do not roll over", ["They roll over for a year", "They apply only to bots", "They replace the user license"], "The policy describes monthly pooled allowances without rollover."),
        q("A 25-minute shift overlap on concurrent licensing:", "Is disregarded", ["Sets the bill", "Deletes the users", "Forces CX 4"], "It is shorter than 30 minutes."),
    ],
    [("30 minutes", "Shorter peaks are ignored."), ("One org", "Do not sum peaks across orgs."), ("Highest level", "The priciest assignment in the period wins."), ("Fair use", "Monthly pool, no rollover. Read the live table.")],
    "Mark a sample week",
    ["Sketch three shifts with a 20-minute overlap and a 45-minute overlap.", "Say which overlap can set the peak.", "Say what happens if someone was CX 3 for a week and CX 1 after.", "Open the fair use policy and find the word allocation."],
    "You can explain a concurrent invoice without inventing a per-minute login charge.",
    ("Inflated peak", "Finance sees a concurrent count equal to two full shifts.", "Overlap of the handoff: 50 minutes, every day.", "The 30-minute discard does not apply. The plateau is real.", "Stagger the handoff under 30 minutes or buy the peak you actually need."),
))

add(lesson(
    "o-packages", "Pick CX 1, CX 2, CX 3, or CX 4 on purpose", "Core", 12,
    "Match the package to the job. Do not buy CX 1 and then design a WFM project.",
    [
        "Use the overview as the menu. Voice-only operations fit CX 1. Omnichannel plus quality fits CX 2. Scheduling, forecasting, and the transcription minutes that WEM expects fit CX 3. Agent Copilot and Journey Management, plus the published token counts, fit CX 4.",
        "The fair use policy also names other commercial shapes, including Communicate, digital package variants, and EX, plus hourly user types. Those names exist on the policy. Their current allowances are rows in that table, not numbers this lab copies. Agent Copilot’s own article describes knowledge, transcripts, scripts, next best action, forms, and written notes. That feature list is the copilot article, and the package that includes it is the overview.",
    ],
    cites("overview", "fair", "copilot"),
    fig("Match the work to the first package that contains it.", [
        ("v", "Voice", "phone", 14, 50),
        ("d", "Digital + QM", "queue", 38, 50),
        ("w", "WEM", "wem", 62, 50),
        ("a", "Copilot", "bot", 84, 50),
    ], [("v", "d"), ("d", "w"), ("w", "a")]),
    "A scoping conversation",
    [
        ("Seller", "Buyer", "Voice only?", "CX 1 if digital and WEM are out of scope.", "Secure IVR is included"),
        ("Buyer", "Seller", "Email and QM", "CX 2 adds digital and quality.", "CX 1 is not enough"),
        ("Buyer", "Seller", "Schedules", "CX 3 adds WEM.", "Transcription minutes too"),
        ("Buyer", "Seller", "Copilot", "CX 4 adds Agent Copilot and tokens.", "30 named, 39 concurrent"),
        ("Buyer", "Policy", "Allowances", "Read fair use before you model overage.", "Do not memorize last year’s rate"),
    ],
    [
        q("A contact center that only takes calls and does not need QM or WEM starts at:", "CX 1", ["CX 3", "CX 4", "EX only"], "The overview describes CX 1 as the voice package."),
        q("Quality management shows up at which package in the overview’s stack?", "CX 2, and therefore also in CX 3 and CX 4", ["CX 1 only", "Nowhere", "AppFoundry only"], "CX 2 adds quality. Higher packages include it."),
        q("Agent Copilot’s article says it can write which of these?", "Notes, including reason, resolution, and possible wrap-up codes", ["SIP INVITEs", "Edge firmware", "Number plans"], "That list is on the copilot overview."),
        q("Journey Management is named on which package?", "CX 4", ["CX 1", "CX 2", "The RFC set"], "The overview places it on CX 4."),
        q("Communicate and hourly user types are documented where?", "The fair use policy", ["RFC 3261", "The bullseye article", "The Edge group article"], "The policy names those commercial shapes."),
        q("Why does this lab refuse to print the per-minute overage price?", "The fair use table changes, and the page is the source", ["Prices are secret", "There is no policy", "Overage is forbidden"], "Link the policy. Do not freeze the card."),
    ],
    [("CX 1", "Voice."), ("CX 2", "Digital and quality."), ("CX 3", "WEM and transcription minutes."), ("Copilot", "Knowledge, transcript, scripts, next best action, forms, notes.")],
    "Scope one statement of work",
    ["List the channels.", "List whether QM, WFM, or Copilot is in scope.", "Name the lowest package that covers the list.", "Link the fair use policy instead of typing a price."],
    "The statement of work names a package someone can find on the overview.",
    ("Copilot on CX 2", "Agents were promised live suggested articles. The org is CX 2.", "Overview: Agent Copilot is a CX 4 addition.", "The package does not include the feature that was sold.", "Change the design or the licenses, and re-read both articles before you commit."),
))

add(lesson(
    "o-people", "People, queues, and the 5,000 member line", "Core", 11,
    "Users live in the org. Queue membership is not the same thing as a division, and it has a hard cap.",
    [
        "Create the person, place them in a division, and grant a role. Membership on a queue is a further step, capped at 5,000 members, and the queue itself sits in one division. A person can be a member of a queue only if your access model lets you see both.",
        "Stations and phones come later, with Edge groups and WebRTC trunks. Do not block org design on hardware. Do decide which division owns the queue before agents are added, because moving it later changes who can administer it.",
    ],
    cites("queues", "divisions", "edge-trunk"),
    fig("User, division, and queue membership are three different joins.", [
        ("user", "User", "agent", 16, 40),
        ("div", "Division", "region", 46, 22),
        ("q", "Queue", "queue", 46, 70),
        ("phone", "Phone later", "phone", 80, 40),
    ], [("user", "div"), ("user", "q"), ("q", "div")]),
    "Add an agent without mixing up the joins",
    [
        ("Admin", "User", "Create", "The person exists in the org.", "Division selected"),
        ("Admin", "Role", "Grant", "They can sign in and see the right objects.", "Pair with division"),
        ("Admin", "Queue", "Add member", "Membership is capped at 5,000.", "Name has no special characters"),
        ("Admin", "Phone", "Defer", "WebRTC or a SIP phone trunk comes with the Edge group.", "Not required to test routing logic"),
    ],
    [
        q("Queue membership is limited to:", "5000", ["200", "50", "1"], "The queue article states 5,000."),
        q("The queue’s division and the user’s role division should be thought of as:", "The access path that lets an admin see the queue they are editing", ["The same field", "A SIP header", "A wrap-up code"], "Divisions control who can see the object."),
        q("A queue name must be:", "Unique and free of special characters", ["Globally unique across all Genesys customers", "Exactly 200 characters", "A phone number"], "Uniqueness is inside the org. 200 characters is the flow-name limit, not the queue rule stated here."),
        q("WebRTC phone trunks are configured with which object?", "An Edge group, including for premises", ["A WFM business unit", "An evaluation form", "A topic"], "The Edge group article covers phone trunks, including WebRTC."),
        q("Moving a queue to another division:", "Changes which role grants can see it", ["Duplicates the members", "Changes the AWS region", "Publishes Architect"], "The object belongs to one division."),
        q("On Queue is required before ACD will:", "Offer interactions to that agent", ["Create the user", "Buy a DID", "Issue an OAuth secret"], "Membership alone is not the routing status."),
    ],
    [("5,000", "Members per queue."), ("Three joins", "User, division grant, queue membership."), ("Name", "Unique, no special characters."), ("Phones", "Edge group work, not the first org task.")],
    "Add a paper agent",
    ["Name the division.", "Name the queue and check the character rule.", "Add the agent as a member.", "Write the status they must select."],
    "A second person could follow your notes and not exceed the cap.",
    ("Member cap", "The import stops at the end of a large skill group.", "Queue members: 5000. Import file: 5001.", "The platform limit is 5,000 members on one queue.", "Split the population across queues or remove stale members before the import."),
))

add(lesson(
    "o-fair", "Fair use is a pool, not a mystery invoice", "Core", 12,
    "Licenses include monthly allowances. Overage is priced on the policy page. Copying the numbers into a design doc freezes them wrong.",
    [
        "The fair use policy describes consumption on top of the user license: BYOC Cloud minutes, data storage, basic routing and IVR, API requests, voice transcription, BYO SMS, workitems, and Journey Management events are among the families on that page. Allowances are monthly, they pool across users, and they do not roll over. Named, concurrent, and hourly user types are all in the policy’s language.",
        "API calls made with a client-credentials integration count toward the API allowance. A lab that polls conversations every second is a bill, not a demo. Transcription minutes are a different meter from the user license, which is why CX 3 calls them out separately. When you estimate, open the policy and read the row. Do not reuse a figure from this paragraph.",
    ],
    cites("fair", "overview", "cc-grant"),
    fig("Several meters sit beside the user license.", [
        ("user", "User license", "agent", 16, 40),
        ("ivr", "IVR", "architect", 40, 20),
        ("api", "API", "trunk", 40, 60),
        ("tr", "Transcript", "wem", 70, 20),
        ("byoc", "BYOC min", "phone", 70, 60),
    ], [("user", "ivr"), ("user", "api"), ("user", "tr"), ("user", "byoc")]),
    "Notice a meter before it notices you",
    [
        ("App", "API", "Poll", "Each request can count.", "Client credentials is still an API call"),
        ("Flow", "IVR", "Minutes", "Basic routing and IVR have an allowance.", "Overage is on the policy"),
        ("Trunk", "BYOC", "Answered calls", "The policy describes how BYOC minutes are measured.", "Read the current rule"),
        ("CX 3", "Transcript", "Another meter", "Voice transcription is not the same as the seat.", "CX 3 includes minutes"),
        ("Finance", "Month end", "No rollover", "Unused allowance does not carry.", "Pool is across users"),
    ],
    [
        q("Fair use allowances roll over to the next month?", "No", ["Yes", "Only API calls", "Only CX 4"], "The policy describes monthly allowances without rollover."),
        q("A client-credentials integration’s API calls are:", "Still API usage against the allowance", ["Free because there is no user", "Billed as SIP", "Ignored under 1,000"], "The token type does not make the call free."),
        q("Voice transcription minutes are:", "A separate meter from the seat, called out on CX 3 and in fair use", ["Included without limit on CX 1", "An RFC", "A queue setting only"], "Both the overview and the policy treat transcription as usage."),
        q("The right way to quote an overage rate in a design is:", "Link the live fair use policy", ["Paste a number from memory", "Use the 2023 matrix price", "Invent a round dollar"], "The table is the source."),
        q("Allowances are pooled across:", "Users in the org for that month", ["All customers in the region", "Only concurrent users worldwide", "Only bots"], "The policy pools across the org’s users."),
        q("Journey Management events show up as a meter for which package story?", "They are a fair-use family, and Journey Management itself is a CX 4 capability", ["They are free on CX 1", "They replace queues", "They are DTMF"], "Overview places the feature on CX 4. The policy meters events."),
    ],
    [("Pool", "Monthly, across users, no rollover."), ("Meters", "IVR, API, storage, BYOC, transcription, SMS, and others."), ("Do not copy rates", "The policy page is the quote."), ("API", "Client-credentials calls still count.")],
    "List the meters your design will touch",
    ["Name every API your integration will call and how often.", "Name whether calls are BYOC or Genesys Cloud Voice.", "Name whether you will transcribe.", "Open the policy and find those rows without writing the prices down."],
    "You have a meter list and a link, not a stale rate card.",
    ("Polling bill", "API overage appears in the first month of a new dashboard.", "Job: GET conversations every second, all day.", "That is on the order of millions of requests. The policy prices API requests.", "Poll on an event or lengthen the interval, and read the allowance before you ship the job."),
))

add(lesson(
    "o-bootstrap", "A first-week admin checklist", "Core", 14,
    "Week one is region, divisions, roles, packages, one queue, and a published in-queue flow. Telephony can follow.",
    [
        "Create or confirm the org in the right core region. Create the divisions you will actually administer. Grant roles in pairs. Assign packages that match the scope. Create one queue with a legal name, a division, a language if you need one, and fewer than 5,000 members. Publish the default in-queue call flow or the queue will be silent.",
        "Then decide Genesys Cloud Voice versus BYOC, because emergency responsibility changes with that choice. Do not create a client-credentials OAuth client with All-division admin “just for now.” The subset rule exists so that temporary clients do not become the back door.",
    ],
    cites("regions", "divisions", "queues", "inqueue", "overview", "oauth"),
    fig("Week one objects, in an order that avoids a silent queue.", [
        ("reg", "Region", "region", 10, 40),
        ("div", "Divisions", "queue", 28, 40),
        ("lic", "Packages", "wem", 46, 40),
        ("q", "Queue", "queue", 64, 40),
        ("flow", "Publish", "architect", 82, 40),
    ], [("reg", "div"), ("div", "lic"), ("lic", "q"), ("q", "flow")]),
    "The first week, object by object",
    [
        ("Admin", "Region", "Confirm login", "Users must use the org’s login host.", "Write it in the runbook"),
        ("Admin", "Divisions", "Create", "Home stays. Add only the splits you will grant.", "Move queues on purpose"),
        ("Admin", "Packages", "Assign", "CX 3 if WEM is in scope.", "CX 4 if Copilot is"),
        ("Admin", "Queue", "Create", "Unique name, division, members.", "5,000 cap"),
        ("Admin", "In-queue", "Publish", "The default call flow is inert until then.", "Digital flows are separate"),
    ],
    [
        q("The default in-queue call flow on day one is:", "Present and unpublished until you publish it", ["Already taking calls", "Impossible to publish", "Only for email"], "The in-queue article is clear about the publish step."),
        q("The safest OAuth client on day one is:", "Client credentials with a narrow role and division", ["Implicit grant with All division", "A shared user password", "No permissions and a hope"], "Narrow pairs match the developer guide. Implicit is deprecated after 25 May 2026."),
        q("WEM in the statement of work means the package conversation starts at:", "CX 3", ["CX 1", "A satellite region", "RFC 3550"], "The overview puts WEM on CX 3."),
        q("Home division on day one should be:", "Left in place. It cannot be deleted.", ["Deleted", "Renamed to the AWS region", "Turned into a queue"], "The divisions article forbids deleting Home."),
        q("Queue creation requires you to choose:", "A division, among other fields", ["An RTP port", "A bullseye ring only", "A PSAP"], "The queue is a configuration object in a division."),
        q("Emergency ownership depends on:", "Whether calls use Genesys Cloud Voice or a BYOC trunk", ["The font size in Architect", "The quiz score", "The wrap-up code"], "The BYOC emergency article separates those responsibilities."),
    ],
    [("Publish", "Or the hold experience does not exist."), ("Narrow client", "Subset of the creator, one division."), ("Package", "Match CX 1–4 to the scope."), ("Home", "Keep it.")],
    "Run the checklist on paper",
    ["Write the login URL.", "Name two divisions.", "Name the package.", "Name the queue and the in-queue publish step.", "Name the OAuth division if you need an integration."],
    "Another admin can execute the list without a meeting.",
    ("Silent day one", "The pilot queue rings agents, but callers hear nothing while they wait.", "Default in-queue flow: not published.", "Unpublished is the documented default state.", "Publish it, place a test call, and only then invite the pilot group."),
))

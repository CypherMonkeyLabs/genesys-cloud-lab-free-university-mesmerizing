from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "edge",
    "title": "The Edge and BYOC Premises",
    "kicker": "Premises",
    "accent": 2,
    "summary": "Premises Edges, Edge groups, phone trunks, sites, and what happens when the local Edge is down.",
    "lessons": [],
}
def add(item):
    TRACK["lessons"].append(item)

add(lesson(
    "e-role", "The premises Edge is the local media hop", "Core", 12,
    "BYOC Premises puts an Edge on your network. Phones and trunks registered there do not need a public address the way BYOC Cloud does.",
    [
        "An Edge group is a set of premises Edges on a low-latency network. Phones on those Edges can call each other, and a trunk plugged into one Edge can be used by the others in the group. That sharing is the point of the group. A single Edge with no group is a single point of failure for every phone that depends on it.",
        "This is a different product from BYOC Cloud. Cloud trunks terminate in AWS. Premises trunks terminate on the Edge. Emergency calling can still be internet-based in some premises designs, and the same Genesys warning applies: if the call rides a BYOC trunk, Genesys is not the emergency provider.",
    ],
    cites("edges", "emergency", "byoc-overview"),
    fig("Phones share a trunk through the Edge group.", [
        ("p1", "Phone", "phone", 14, 30),
        ("p2", "Phone", "phone", 14, 70),
        ("e", "Edge group", "edge", 48, 46),
        ("t", "Trunk", "trunk", 80, 46),
    ], [("p1", "e"), ("p2", "e"), ("e", "t")]),
    "Put the trunk where the group can see it",
    [
        ("Engineer", "Edge", "Place on the LAN", "Low latency to the phones.", "The group definition"),
        ("Engineer", "Group", "Add the Edge", "The Edge inherits group phone trunks.", "Confirm inherit on the interface"),
        ("Carrier", "Trunk", "One Edge", "Other Edges in the group can use it.", "That is the documented benefit"),
        ("Safety", "Power", "Local", "A dead Edge is a local outage.", "Cloud trunks are a different path"),
    ],
    [
        q("An Edge group exists so that:", "Edges can share phones and trunks on a low-latency network", ["The org can change AWS regions", "OAuth secrets replicate", "WFM forecasts faster"], "The overview lists sharing as the benefit."),
        q("A trunk on one Edge in the group is:", "Usable by the other Edges in that group", ["Invisible to them", "A cloud trunk automatically", "A division"], "The article says members share endpoints."),
        q("BYOC Cloud and BYOC Premises differ because:", "Cloud terminates in AWS. Premises terminates on an Edge.", ["They are the same SKU", "Premises has no SIP", "Cloud has no RTP"], "Keep the two products apart."),
        q("Inheriting phone trunks is confirmed on:", "The Edge network interface, Inherit from Edge Group", ["The fair use page", "The quiz", "The bot flow"], "The create-group article tells you to confirm that setting."),
        q("A single Edge with every phone registered to it is:", "A local single point of failure", ["Required", "A satellite region", "A CX 4 token"], "The group exists so one device is not the whole site."),
        q("Emergency calls that use the premises BYOC trunk are:", "Still under the BYOC warning. Genesys is not the emergency provider.", ["Guaranteed by the Edge serial number", "Routed as GCV automatically", "Blocked"], "The emergency article covers both BYOC models."),
    ],
    [("Group", "Share phones and trunks."), ("Inherit", "The Edge takes the group’s phone trunks."), ("Cloud vs premises", "AWS versus an Edge."), ("Emergency", "Still your carrier if the trunk is BYOC.")],
    "Draw one site",
    ["Name two Edges.", "Name the shared trunk.", "Say what a phone on Edge B uses.", "Say who owns emergency."],
    "The picture shows a group, not a single box.",
    ("Trunk on the wrong Edge", "Phones on Edge B cannot seize the carrier.", "Edge B phone trunks: Use the following trunks, empty. Group trunk: attached only in the group, inherit not selected.", "The Edge is not inheriting.", "Select Inherit from Edge Group, or explicitly add the trunk, then test."),
))

add(lesson(
    "e-site", "Local site routing stays home until it cannot", "Core", 12,
    "Genesys uses Edges in the same site when it can. Another site is the exception.",
    [
        "The Edge group article says local site routing prefers same-site Edges to save bandwidth and latency. Another site is used when local Edges are offline, already at capacity, or do not hold the resource, such as the agent, the station, or the trunk.",
        "A site is also where number plans and outbound routes live, and where you attach a location. Building two sites and one giant Edge group across a slow WAN fights the article. The group wants a low-latency network. The site wants local media. Those sentences should agree.",
    ],
    cites("edges", "byoc-quick", "numbers"),
    fig("Same-site Edges first. The other site is a documented exception.", [
        ("a", "Site A", "edge", 22, 40),
        ("b", "Site B", "edge", 70, 40),
        ("call", "Call", "phone", 46, 16),
    ], [("call", "a")]),
    "Keep the call on the site",
    [
        ("Call", "Site A", "Local Edge", "Preferred path.", "Bandwidth stays home"),
        ("Edge A", "Capacity", "Full", "Then another site may be used.", "Documented exception"),
        ("Edge A", "Offline", "Failover", "Also an exception.", "Not the steady state"),
        ("Trunk", "Only on B", "Resource exception", "The call may cross because the trunk is not local.", "Place trunks where the calls are"),
    ],
    [
        q("Local site routing prefers:", "Edges in the same site", ["The farthest satellite", "A random Edge", "The Home division"], "The article says same-site first."),
        q("Another site is used when local Edges are:", "Offline, at capacity, or missing the resource", ["In the same rack", "Newer", "Running WebRTC"], "Those are the three documented exceptions."),
        q("A trunk that exists only at site B will:", "Pull calls toward B when that trunk is required", ["Be ignored", "Delete site A", "Become GCV"], "The resource exception covers a trunk that is not local."),
        q("An Edge group stretched across a high-latency WAN:", "Conflicts with the low-latency group definition", ["Is required", "Is a number plan", "Is an OAuth grant"], "The group article wants low latency."),
        q("Number plans are attached at:", "The site", ["The agent profile", "The bot", "The token"], "The number-plan article is a site feature."),
        q("Steady-state design should:", "Put Edges, phones, and the trunks they need in the same site", ["Hairpin every call", "Use one Edge worldwide", "Disable local routing"], "Exceptions are for failure, not for the happy path."),
    ],
    [("Same site", "The preferred path."), ("Three exceptions", "Offline, capacity, missing resource."), ("Low latency", "What a group is for."), ("Plans", "Live on the site.")],
    "Place a trunk",
    ["Name the site where the agents sit.", "Put the trunk there.", "Name the three reasons a call may leave.", "Say why a WAN-wide group is a bad default."],
    "The happy path is local.",
    ("Hairpin by design", "Every branch call traverses the headquarters WAN.", "Branch Edges: offline in the design. Only the HQ Edge exists.", "The exception has been made the architecture.", "Put an Edge and the local trunk in the branch, and let HQ be the failure path."),
))

add(lesson(
    "e-phone", "Phone trunks, WebRTC, and inherit", "Core", 11,
    "WebRTC and SIP phones are phone trunks on the Edge group. Inherit is the default you should verify.",
    [
        "The create-group article has you select a WebRTC or SIP phone trunk on the group. Each Edge can inherit that list. The advanced path is to ignore the group and pin trunks on one Edge’s network interface. Pinning is how a phone becomes stranded when that one Edge dies.",
        "WebRTC phones still need a working path to the Edge or cloud media that hosts them. They are not a reason to skip the site and the location. A browser phone at home is a network design, not only a checkbox.",
    ],
    cites("edge-trunk", "edges"),
    fig("Inherit the group phone trunk unless you mean to pin it.", [
        ("g", "Group trunk", "trunk", 22, 40),
        ("e1", "Edge A inherit", "edge", 58, 22),
        ("e2", "Edge B pin", "edge", 58, 70),
    ], [("g", "e1")]),
    "Verify inherit before the pilot",
    [
        ("Admin", "Group", "Add WebRTC trunk", "The article’s phone-trunk field.", "SIP phones are the same list"),
        ("Admin", "Edge", "Network interface", "Confirm Inherit from Edge Group.", "The article tells you to look"),
        ("Admin", "Pin", "Only with a reason", "Use the following trunks is the override.", "Write the reason down"),
        ("Test", "Both Edges", "Register a phone", "A phone should survive one Edge if the group is real.", "Otherwise you pinned it"),
    ],
    [
        q("The default the article tells you to confirm is:", "Inherit from Edge Group", ["Use the following trunks, empty", "No phone trunk", "A cloud-only DID"], "Inherit is the documented default behavior."),
        q("WebRTC is configured as:", "A phone trunk on the Edge group", ["A wrap-up code", "A bullseye ring", "A fair-use token"], "The article includes WebRTC in the phone-trunk picker."),
        q("Pinning a phone trunk to one Edge means:", "The other Edges do not provide that phone path", ["Automatic failover", "A second region", "A published flow"], "Override is local to that interface."),
        q("The menu path in the article includes:", "Telephony, Edge Groups, or the Edge network interface for the override", ["WFM, forecasts", "Quality, evaluations", "OAuth, tokens"], "Those are the telephony admin pages named."),
        q("A home WebRTC user still needs:", "A designed path to the media that hosts the phone", ["Nothing", "A premises headset server always", "CX 4"], "The checkbox is not the network."),
        q("A pilot that only tests one Edge:", "Does not prove group failover", ["Proves DCVP", "Proves emergency", "Proves predictive routing"], "Fail one Edge on purpose in a maintenance window."),
    ],
    [("Inherit", "Confirm it."), ("Pin", "An override with a reason."), ("WebRTC", "A phone trunk."), ("Test", "Both Edges.")],
    "Check one interface",
    ["Say where inherit is displayed.", "Say what the override is called.", "Say how you would test failover.", "Say why a home user is still a network design."],
    "Inherit is either confirmed or deliberately replaced.",
    ("Empty override", "New phones will not register on Edge B.", "Phone trunks: Use the following trunks. List: empty. Group: WebRTC trunk present.", "The override replaced inherit with nothing.", "Select Inherit from Edge Group."),
))

add(lesson(
    "e-fail", "When the local Edge is offline", "Core", 12,
    "The documented failover is another site, if that site actually has the resource.",
    [
        "Offline, at capacity, or missing the resource: those are the only reasons the article gives for leaving the site. If site B has no trunk and no path to the agent’s station, failover has nowhere to go. Capacity is a real limit. Filling every Edge to the ceiling makes the failure path the normal path.",
        "Cloud callers on a BYOC Cloud trunk do not use this Edge at all. An Edge outage and a cloud trunk outage are different incidents. The topology in this lab lets you toggle them separately so the two stories stay apart.",
    ],
    cites("edges", "byoc-overview"),
    fig("Offline local Edges, then the other site, and only if the resource is there.", [
        ("a", "Site A down", "edge", 20, 40),
        ("b", "Site B", "edge", 55, 40),
        ("c", "Cloud trunk", "trunk", 84, 40),
    ], [("a", "b")]),
    "Fail one site in a maintenance window",
    [
        ("Ops", "Edge A", "Take offline", "Local phones must move or fail.", "Documented"),
        ("Ops", "Site B", "Check the trunk", "No trunk means no failover for that call.", "Resource exception works both ways"),
        ("Ops", "Cloud DID", "Separate test", "It should still ring.", "It does not use the Edge"),
        ("Ops", "Capacity", "Watch the steady state", "If you always overflow, you are out of capacity.", "Add Edges or calls"),
    ],
    [
        q("A cloud BYOC caller during a premises Edge outage:", "Can still be served by the AWS media tier", ["Always drops", "Becomes a satellite org", "Loses their division"], "Different path."),
        q("Failover to another site fails when:", "That site does not hold the trunk, station, or agent you need", ["The site has a name", "The flow is published", "The queue has a description"], "The resource has to exist there."),
        q("Capacity failover means:", "Local Edges are already full, so another site is allowed", ["The bill is concurrent", "The bot timed out", "The code is ININ-WRAP-UP-TIMEOUT"], "It is one of the three exceptions."),
        q("Making overflow the normal path means:", "You are running at capacity all the time", ["Local routing is healthy", "DCVP is off", "Skills are disregarded"], "The article describes capacity as an exception."),
        q("The three exceptions are:", "Offline, capacity, and missing resource", ["Save, publish, and refresh", "CX 1, CX 2, and CX 3", "UDP, TCP, and TLS only"], "The Edge group article lists them."),
        q("The lab topology separates Edge failure from trunk failure so that:", "You can see which path actually drops", ["Both always drop together", "3D replaces the article", "Failures are decorative"], "They are different products."),
    ],
    [("Three exceptions", "Offline, capacity, missing resource."), ("Cloud path", "Independent of the Edge."), ("Nowhere to go", "The other site must hold the resource."), ("Steady state", "Overflow should not be normal.")],
    "Write the failover test",
    ["State the Edge you will stop.", "State the site that should take the call.", "State the cloud DID that should not care.", "State what you will measure."],
    "The test has a premises case and a cloud case.",
    ("Empty site B", "Edge A dies and branch phones get silence.", "Site B Edges: online. Trunks: none. Stations: none.", "There is no resource to fail over to.", "Put a trunk and a usable path at B, or accept that A is a single point of failure and staff it that way."),
))

add(lesson(
    "e-compare", "Choose Cloud, Premises, or both", "Core", 12,
    "Use premises when the phones and the carrier are on your network. Use cloud when they are not. Use both only where each number has an owner.",
    [
        "BYOC Cloud wants a public carrier and accepts internet RTP. BYOC Premises wants Edges close to phones and trunks. Genesys Cloud Voice wants neither your carrier nor your Edge for those numbers. A design that uses all three is legal and easy to mis-operate if emergency, monitoring, and the DID’s route are not labeled per number.",
        "The quick start, the Edge group article, and the Voice region article are the three pages that justify the choice. A slide that says “hybrid” without those pages is not a design.",
    ],
    cites("byoc-overview", "edges", "gcv-regions", "emergency"),
    fig("Three ways a number can enter the org.", [
        ("g", "GCV", "region", 16, 40),
        ("c", "BYOC Cloud", "trunk", 46, 40),
        ("p", "Premises Edge", "edge", 78, 40),
    ], [("g", "c"), ("c", "p")]),
    "Label every number",
    [
        ("Number", "Model", "One owner", "GCV, cloud trunk, or premises trunk.", "Not “hybrid” as the owner"),
        ("Emergency", "Owner", "Named", "Genesys for GCV. Carrier for BYOC.", "Written down"),
        ("Monitor", "Path", "Named", "Cloud media page, or the Edge.", "Different consoles"),
        ("Site", "Local", "If premises", "Same-site Edges.", "Cloud skips this"),
    ],
    [
        q("A number’s carrier model should be:", "One of GCV, BYOC Cloud, or BYOC Premises, written down", ["Always all three", "Implied by the queue name", "Chosen by bullseye"], "Hybrid is a mix of numbers, not a mix inside one number."),
        q("Internet RTP is a reason to hesitate about:", "BYOC Cloud", ["A local Edge on a quiet LAN", "A wrap-up code", "A division"], "The cloud overview tells you to judge the internet."),
        q("Phones on a private LAN with a local carrier fit:", "BYOC Premises", ["A satellite org", "A bot flow", "Fair use only"], "The Edge is the local hop."),
        q("Emergency ownership for a BYOC number is:", "The carrier, with Genesys’ warning in view", ["Automatically Genesys", "The WFM business unit", "The OAuth client"], "The emergency article."),
        q("“Hybrid” without a per-number table is:", "Not a design yet", ["Required by RFC 3261", "The CX 4 token", "A published flow"], "Label the numbers."),
        q("The three articles that justify the choice are:", "BYOC Cloud overview, Edge groups, and Genesys Cloud Voice regions", ["Three quiz pages", "Three RFCs only", "Three certifications only"], "Read those before the slide."),
    ],
    [("Per number", "Name the model."), ("Cloud", "Public carrier, internet RTP."), ("Premises", "Edge, local trunks."), ("GCV", "Genesys is the carrier.")],
    "Label five numbers",
    ["Write the model for each.", "Write the emergency owner.", "Write which console you would open.", "Say which article you used."],
    "The table has no row labeled only “hybrid.”",
    ("Unlabeled DID", "An outage bridge cannot tell which carrier to call.", "DID inventory: model column empty.", "The design never assigned an owner.", "Fill the column from the trunk or the GCV number list before the next change window."),
))

add(lesson(
    "e-webrtc-net", "A browser phone is still a network endpoint", "Core", 11,
    "WebRTC removes the desk set. It does not remove media engineering.",
    [
        "The Edge group article treats WebRTC as a phone trunk. The BYOC Cloud overview treats internet RTP as something you must judge. A browser at home is both: a WebRTC endpoint whose packets cross whatever network the agent is actually on. Split tunneling, a full VPN, and a hotel network are different designs.",
        "Do not debug a home-agent audio problem by editing Architect. Confirm the phone trunk, the Edge or cloud media the phone uses, and the path from the browser. Then look at the flow.",
    ],
    cites("edge-trunk", "byoc-overview", "media-mon"),
    fig("The browser still has a media path.", [
        ("b", "Browser", "phone", 16, 40),
        ("net", "Network", "trunk", 46, 40),
        ("m", "Media", "region", 78, 40),
    ], [("b", "net"), ("net", "m")]),
    "Place the path before the pilot",
    [
        ("Agent", "Browser", "WebRTC", "The phone trunk must exist.", "Inherit or cloud media"),
        ("Network", "Path", "VPN or split", "Pick one on purpose.", "Hotel Wi-Fi is a test case"),
        ("Ops", "Monitor", "Media page or Edge", "Look there first.", "Not the prompt"),
        ("Flow", "Later", "If signaling is fine", "Then read Insights.", "Order matters"),
    ],
    [
        q("WebRTC is documented as:", "A phone trunk", ["A queue evaluation method", "A certification", "A number-plan match type"], "The Edge group article includes it."),
        q("Home-agent audio is first a question about:", "The path from the browser to media", ["The wrap-up code text", "The bullseye delay", "The quiz"], "Architect did not move the packets."),
        q("Internet quality is called out for:", "BYOC Cloud RTP, and it applies to any media that crosses the internet", ["Only fax", "Only SMS", "Only surveys"], "The overview’s warning is about RTP on the internet."),
        q("A full-tunnel VPN and split tunnel are:", "Different paths you should choose explicitly", ["The same thing", "Both forbidden", "Both DCVP toggles"], "Write the choice down."),
        q("Monitor cloud media resources helps when:", "The phone’s media is in the cloud", ["The agent forgot On Queue only", "You are editing a prompt", "You are buying tokens"], "Use the console that matches the path."),
        q("Editing the in-queue prompt to fix one-way audio is:", "The wrong first move", ["Required", "The DCVP migration", "The 30 day rule"], "Prove the media path first."),
    ],
    [("WebRTC", "A phone trunk."), ("Path", "VPN, split, or local. Choose."), ("Console", "Edge or cloud media."), ("Flow last", "If signaling is already fine.")],
    "Describe one home agent",
    ["Where the browser is.", "Which phone trunk.", "Which network path.", "Which console you would open."],
    "The home agent has a path, not only a laptop.",
    ("VPN hairpin", "Home agents sound worse than branch agents on the same queue.", "Browsers: full-tunnel VPN to HQ, then back out to cloud media.", "The path is twice as long as it needs to be.", "Test split tunnel for media, with security’s sign-off, and compare the cloud media monitor."),
))

add(lesson(
    "e-checklist", "Premises turn-up checklist", "Core", 12,
    "Group, inherit, site, trunk, failover test, emergency owner.",
    [
        "Create the Edge group on a low-latency network. Add the phone trunk. Confirm inherit on every Edge. Put the carrier trunk where the calls are. Attach the site’s location and number plans. Run one failover test and one cloud-trunk test so you know they are different. Write the emergency owner on the same page.",
        "None of those steps is an Architect publish. You can build the flow in parallel. You cannot let the flow be the only test.",
    ],
    cites("edges", "edge-trunk", "emergency", "numbers"),
    fig("The checklist ends in two test calls, not in a diagram.", [
        ("g", "Group", "edge", 16, 40),
        ("s", "Site", "region", 40, 40),
        ("t", "Test", "phone", 66, 40),
        ("e", "Emergency", "carrier", 88, 40),
    ], [("g", "s"), ("s", "t"), ("t", "e")]),
    "Turn up a branch",
    [
        ("Build", "Group", "Low latency", "Edges that can share.", "Not across a slow WAN"),
        ("Build", "Inherit", "Confirmed", "Every interface.", "No empty override"),
        ("Build", "Trunk and plans", "On the site", "Local resource.", "Emergency route included"),
        ("Test", "Fail one Edge", "And one cloud DID", "Two outcomes.", "Write them down"),
    ],
    [
        q("The checklist’s failover test and cloud test are:", "Both required, because they prove different paths", ["The same test", "Optional if the flow is published", "Replaced by a quiz"], "Edge failure and cloud trunk failure are different."),
        q("Inherit must be checked:", "On each Edge interface", ["Once per org", "Only in Architect", "Only in WFM"], "The setting is per Edge."),
        q("Number plans and the location attach to:", "The site", ["The OAuth client", "The evaluation form", "The bot intent"], "Telephony site objects."),
        q("A slow WAN between Edges in one group violates:", "The low-latency definition of a group", ["The 200 character flow name", "The 80/20 predictive split", "RFC 5737"], "Keep the group local."),
        q("Emergency is on the checklist because:", "BYOC trunks are not Genesys emergency service", ["Edges block 911", "Plans forbid 911", "Queues forbid 911"], "The warning belongs on the turn-up page."),
        q("Architect publish proves the Edge group?", "No", ["Yes", "Only for bots", "Only after 30 days"], "Place a call."),
    ],
    [("Group", "Low latency."), ("Inherit", "Every Edge."), ("Site", "Trunk, plans, location."), ("Two tests", "Edge down, and a cloud DID.")],
    "Sign the checklist",
    ["Group and site names.", "Inherit confirmed.", "Emergency owner.", "Two test results."],
    "A second engineer could repeat the test.",
    ("Untested failover", "The design review passed on a diagram. The first real Edge failure dropped the branch.", "Test log: empty.", "The exception path was never exercised.", "Run the failover in a window and attach the result to the design."),
))

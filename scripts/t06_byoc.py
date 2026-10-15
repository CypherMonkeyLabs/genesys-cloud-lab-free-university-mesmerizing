from cites import cites
from lessonlib import fig, lesson, q

TRACK = {
    "id": "byoc",
    "title": "BYOC Cloud and SIP trunks",
    "kicker": "Telephony",
    "accent": 4,
    "summary": "Carrier and PBX trunks, RTP over the internet, Dynamic Cloud Voice, and the quick-start order.",
    "lessons": [],
}
def add(item):
    TRACK["lessons"].append(item)

add(lesson(
    "b-what", "BYOC Cloud is your carrier, Genesys’ media", "Core", 12,
    "You bring the carrier contract. Genesys terminates a SIP trunk on the AWS media tier. Audio is RTP on the internet.",
    [
        "The overview says you create the trunk in Telephony Admin between Genesys Cloud media resources in AWS and a third-party carrier or device. That far end can be another cloud or a box on prem, but it needs a public address and open ports. There is no customer Edge hardware in the pure BYOC Cloud path.",
        "Because RTP crosses the public internet, the overview tells you to judge latency and loss before you commit. Genesys Cloud Voice is the other choice: Genesys is the carrier, including emergency services on numbers you buy there. Mixing them does not copy emergency data from Genesys Cloud Voice into your BYOC carrier.",
    ],
    cites("byoc-overview", "byoc", "emergency"),
    fig("Public SIP and RTP between the carrier and the media tier.", [
        ("c", "Carrier", "carrier", 16, 40),
        ("sip", "SIP", "trunk", 46, 22),
        ("rtp", "RTP", "phone", 46, 68),
        ("m", "Media tier", "region", 80, 40),
    ], [("c", "sip"), ("sip", "m"), ("c", "rtp"), ("rtp", "m")]),
    "Decide Cloud versus Genesys as the carrier",
    [
        ("Buyer", "Contract", "Who bills the minutes", "BYOC means you hold the carrier contract.", "GCV means Genesys does"),
        ("Engineer", "Address", "Public IP", "The far end must be reachable.", "RFC 1918 alone will not do"),
        ("Engineer", "RTP", "Internet", "Plan for latency.", "SRTP is still RTP"),
        ("Safety", "Emergency", "Separate", "GCV emergency data is not handed to the BYOC carrier.", "You must tell the carrier"),
    ],
    [
        q("BYOC Cloud places the trunk between:", "The AWS media tier and your carrier or PBX", ["Two agents’ browsers only", "WFM and QM", "A satellite and Home"], "The overview describes that path."),
        q("The far end must have:", "A publicly reachable address and open ports", ["Only a private address", "An Architect bot", "A CX 4 token"], "The overview states both requirements."),
        q("The media protocol the overview highlights is:", "RTP over the internet", ["SCIM", "SMTP", "Only SIP with no media"], "SIP sets up. RTP carries audio."),
        q("A pure BYOC Cloud design includes customer Edge hardware?", "No", ["Yes, always", "Only for chat", "Only for surveys"], "The cloud trunk terminates in AWS. Premises Edges are the other product."),
        q("Genesys Cloud Voice emergency information is shared automatically with a new BYOC carrier?", "No. You inform the carrier yourself.", ["Yes", "Only in FedRAMP", "Only for 988"], "The emergency article is explicit."),
        q("Latency belongs in the design because:", "The overview tells you to consider internet quality before you implement", ["Latency is illegal", "Latency is a wrap-up code", "Latency is removed by bullseye"], "It is a design input, not a surprise."),
    ],
    [("You bring", "The carrier contract."), ("Public", "Address and ports."), ("RTP", "Across the internet."), ("Emergency", "Not copied from GCV.")],
    "Write the BYOC decision",
    ["Name the carrier.", "Write the public address you will use in the lab as 192.0.2.10.", "State that 192.0.2.10 is documentation-only.", "State who owns emergency."],
    "The decision names a carrier and an emergency owner.",
    ("Private address", "The trunk never comes in service.", "Far-end address: 10.1.1.20. Path: BYOC Cloud.", "10.0.0.0/8 is not a public address. The overview requires one.", "Give the carrier a public address, or use BYOC Premises with an Edge on that network."),
))

add(lesson(
    "b-types", "Carrier trunks and PBX trunks", "Core", 12,
    "BYOC Carrier and BYOC PBX are the two types. Carrier has subtypes. PBX has one.",
    [
        "The create-trunk article lists BYOC Carrier and BYOC PBX. Carrier subtypes called out there are Generic BYOC Carrier, Genesys Cloud BYOC Verizon, and BYOC WhatsApp Business Calling. PBX has a single subtype. Start from the base settings. Open the advanced sections only when the carrier’s questionnaire says you must.",
        "WhatsApp as a trunk subtype is not the same object as an inbound message flow. One is telephony signaling for WhatsApp Business Calling. The other is Architect routing for messages. Do not collapse them because the brand name matches.",
    ],
    cites("byoc", "byoc-quick"),
    fig("Pick type and subtype before the advanced panels.", [
        ("t", "Type", "trunk", 20, 40),
        ("g", "Generic", "carrier", 50, 20),
        ("v", "Verizon", "carrier", 50, 45),
        ("w", "WhatsApp calling", "phone", 50, 70),
        ("p", "PBX", "edge", 80, 40),
    ], [("t", "g"), ("t", "v"), ("t", "w"), ("t", "p")]),
    "Choose the subtype from the carrier, not from habit",
    [
        ("Admin", "Trunks", "External, Create", "The article’s menu path is Digital and Telephony, Telephony, Trunks.", "External Trunks tab"),
        ("Admin", "Type", "Carrier or PBX", "Carrier faces a provider. PBX faces your switch.", "CUCM would be a PBX conversation"),
        ("Admin", "Subtype", "Generic unless told", "Verizon and WhatsApp calling are specific.", "Do not pick Verizon for a different carrier"),
        ("Admin", "Advanced", "Only if required", "Base settings are the recommendation.", "The questionnaire drives exceptions"),
    ],
    [
        q("The two BYOC Cloud trunk types are:", "BYOC Carrier and BYOC PBX", ["UDP and TCP only", "CX 1 and CX 4", "Home and All"], "The create article names both."),
        q("Generic BYOC Carrier is:", "The subtype for most carrier configurations", ["A Verizon-only mode", "A premises Edge", "A bot flow"], "The article says the generic subtype covers most carriers."),
        q("WhatsApp Business Calling as a trunk subtype is:", "A carrier subtype, not an Architect message flow", ["The inbound message tab", "A WFM activity", "A wrap-up code"], "Keep the telephony object and the flow type apart."),
        q("BYOC PBX subtypes documented in that article:", "One", ["Three", "Five", "Fifty"], "The article says PBX has a single subtype."),
        q("Advanced trunk settings should be opened:", "When the carrier requirements say the base settings are not enough", ["Always, first", "Never, they are decorative", "Only after a region move"], "The article recommends the base settings."),
        q("A CUCM you still operate is most like:", "A PBX reached by a BYOC PBX trunk", ["A Genesys core region", "A bullseye ring", "An OAuth grant"], "The PBX type is the documented fit for your own switch."),
    ],
    [("Two types", "Carrier and PBX."), ("Three carrier subtypes", "Generic, Verizon, WhatsApp Business Calling."), ("Base first", "Advanced only when required."), ("Message flow", "A different object from the WhatsApp calling trunk.")],
    "Pick a type for three neighbors",
    ["A generic SIP carrier.", "Verizon.", "A CUCM cluster you still own.", "Say which one is not an Architect flow."],
    "Each neighbor has a type and a subtype.",
    ("Verizon subtype on the wrong carrier", "Outbound calls fail the carrier’s specific headers.", "Subtype: Genesys Cloud BYOC Verizon. Contract: a different carrier.", "The subtype adds Verizon-specific header work the article mentions.", "Recreate the trunk as Generic BYOC Carrier unless this contract is Verizon."),
))

add(lesson(
    "b-order", "The quick-start order", "Core", 12,
    "Location, trunk, outbound route, number plan. The product on the subscription comes before all of that.",
    [
        "The quick start’s order is the lab’s order. Confirm the org and that BYOC Cloud is on the subscription. Work the carrier requirements. Add a physical location. Create the trunk. Assign it on an outbound route. Genesys creates default outbound routes and still requires you to attach the trunk. Add or adjust number plans for the classifications you dial.",
        "The location is also the emergency story. Skipping it to “test the SIP first” leaves 911 with nowhere honest to point. New trunks should be Dynamic Cloud Voice from the start so you do not migrate them next quarter.",
    ],
    cites("byoc-quick", "dcvp", "numbers", "emergency"),
    fig("The quick start is a sequence, not a pile of screens.", [
        ("l", "Location", "phone", 14, 40),
        ("t", "Trunk", "trunk", 38, 40),
        ("r", "Route", "queue", 62, 40),
        ("n", "Plan", "architect", 84, 40),
    ], [("l", "t"), ("t", "r"), ("r", "n")]),
    "Turn up in order",
    [
        ("Admin", "Subscription", "BYOC Cloud present", "The guide assumes it.", "Do not trunk a voice-less org"),
        ("Admin", "Location", "Physical site", "Required to enable services.", "Emergency uses it"),
        ("Admin", "Trunk", "DCVP", "New trunks use Dynamic Cloud Voice.", "Test trunk before production"),
        ("Admin", "Route", "Assign", "Default routes exist and are empty until you assign.", "Then number plans"),
    ],
    [
        q("Default outbound routes still need:", "A trunk assignment", ["Nothing", "A bot", "A token"], "The quick start says you must assign the trunk."),
        q("The location step is skippable for a lab SIP test?", "No. The guide places it before the trunk, and emergency depends on it.", ["Yes", "Only in US West", "Only for email"], "Do not skip it."),
        q("New trunks should be created on:", "Dynamic Cloud Voice", ["The legacy platform", "An Edge only", "A common module"], "The quick start and the DCVP article agree."),
        q("Number plans come:", "After you can classify what people dial", ["Before the org exists", "Instead of a trunk", "Only for 988"], "The quick start includes them in the telephony build."),
        q("Carrier requirements are:", "A step you do with the carrier, documented beside the quick start", ["Optional folklore", "An RFC only", "A WFM forecast"], "The guide points at the carrier requirements article."),
        q("A trunk with no route assignment shows up as:", "Inbound may work while outbound finds nothing", ["A region outage", "A deleted Home division", "A predictive routing win"], "That split is the classic missed step."),
    ],
    [("Order", "Location, trunk, route, plans."), ("DCVP", "For new trunks."), ("Assign", "Default routes are not finished."), ("Location", "Not optional.")],
    "Write the four steps",
    ["Location.", "Trunk type.", "Which route gets the trunk.", "Which number-plan classification you care about."],
    "The sequence matches the quick start.",
    ("Route left empty", "Agents dial out and hear reorder. Inbound DIDs ring.", "Outbound route trunk: unassigned. External trunk: in service.", "The quick start’s assignment step was skipped.", "Assign the trunk on the outbound route and retry."),
))

add(lesson(
    "b-dcvp", "Dynamic Cloud Voice is the current platform", "Advanced", 13,
    "New trunks start there. Moving an old trunk means allow lists, Amazon root CAs, TLS ciphers, and a toggle.",
    [
        "The DCVP article says to test a new trunk before you move production. Migration is not only a checkbox. You add the egress IP ranges to the carrier or SBC allow list, import Amazon root CAs so the far end trusts the BYOC endpoints, and confirm the TLS cipher list. Then you enable the high-capacity outbound platform on the trunk, and you point the far end’s SIP targets at the new ingress addresses.",
        "The article warns that the Genesys-side toggle is the easy half. The remote SIP endpoint is the hard half. Change the allow list before you flip production, and keep a tested trunk beside the old one until inbound and outbound both complete.",
    ],
    cites("dcvp", "byoc-quick"),
    fig("Allow list and certificates move with the trunk, not after the outage.", [
        ("old", "Old trunk", "trunk", 18, 40),
        ("acl", "ACL and CA", "edge", 48, 22),
        ("new", "DCVP", "region", 78, 40),
    ], [("old", "acl"), ("acl", "new")]),
    "Migrate without a surprise INVITE",
    [
        ("Engineer", "Test trunk", "New, not production", "Prove the carrier path.", "The article prefers this"),
        ("Carrier", "ACL", "Add egress ranges", "So BYOC can send.", "Do this before the flip"),
        ("Carrier", "Trust", "Amazon root CAs", "TLS fails closed without them.", "Cipher list too"),
        ("Admin", "Toggle", "High capacity outbound", "Genesys starts sending from the new egress.", "Then update ingress targets"),
    ],
    [
        q("The article’s preferred way to learn DCVP is:", "A new test trunk, not your first production flip", ["Editing the live trunk at noon", "Deleting the location", "Turning off TLS"], "Test, then migrate."),
        q("Amazon root CAs are imported so that:", "The remote SIP endpoint trusts the BYOC endpoints", ["Agents trust the CRM", "WFM trusts the forecast", "Browsers trust AppFoundry"], "The article lists that trust step."),
        q("The allow list change is:", "Add the egress IP ranges on the carrier or SBC", ["Remove all UDP", "Block the login host", "Allow only 192.0.2.0/24"], "192.0.2.0/24 is documentation space, not the Genesys egress list. Use the article’s addresses."),
        q("The Genesys-side outbound control the article names is:", "Enable high capacity outbound platform", ["Publish the in-queue flow", "Set bullseye to 2 seconds", "Delete the OAuth client"], "That toggle starts the new egress."),
        q("Ingress addresses must be updated on:", "The remote SIP endpoint", ["The agent’s headset", "The wrap-up code", "The division"], "Inbound will not arrive at the new platform otherwise."),
        q("Doing the toggle before the allow list risks:", "Outbound INVITEs that the carrier drops", ["Free tokens", "A deleted Home division", "Automatic GCV emergency"], "The far end has to permit the new sources."),
    ],
    [("Test first", "A new trunk."), ("ACL", "Egress ranges."), ("Trust", "Amazon root CAs and ciphers."), ("Then toggle", "High capacity outbound, then ingress targets.")],
    "Order a migration",
    ["Write test trunk first.", "Write ACL and CA before the toggle.", "Write the ingress update.", "Say why 192.0.2.0/24 is not the allow list."],
    "The order matches the article, and the documentation range is not mistaken for Genesys’ IPs.",
    ("TLS failure after the flip", "OPTIONS and INVITEs fail the handshake.", "Carrier log: unknown CA. Amazon roots not imported.", "The trust step was skipped.", "Import the Amazon root CAs from the DCVP article and retry the test trunk before production."),
    "Copy the IP ranges and cipher names from the current DCVP article. They are operational data and this lab does not duplicate them, because a stale copy would be worse than a link.",
))

add(lesson(
    "b-plans", "Number plans classify what people dial", "Core", 13,
    "A site can hold 200 plans. DIDs do not need one for basic routing. Emergency, extension, and 988 already exist as defaults.",
    [
        "Default classifications in the number-plan article include Emergency (911 and 933 in the United States and Canada, 142 in Switzerland), Extension for 4 to 6 digits, National, International, a regex Network plan, and Suicide Prevention, which routes 988 to +18002738255. Match types include digit length, E.164 list, inter-country, intra-country, number list, and regular expression. Intra-country and inter-country normalize to E.164. Digit length and E.164 lists do not.",
        "You can normalize more than once as a number passes through plans. The product includes a call simulator. Use it. A custom classification is just a name you invent for a group of numbers. The lab’s number desk imitates these rules. It is not that simulator.",
    ],
    cites("numbers", "emergency"),
    fig("A dial string hits a classification, then a route.", [
        ("d", "Dial", "phone", 14, 40),
        ("p", "Plan", "architect", 46, 40),
        ("r", "Route", "trunk", 78, 40),
    ], [("d", "p"), ("p", "r")]),
    "Classify before you route",
    [
        ("Caller", "Site", "Dial 911", "Emergency classification.", "Needs an emergency route"),
        ("Caller", "Site", "Dial 4501", "Extension, 4 to 6 digits.", "No normalization"),
        ("Caller", "Site", "Dial a national number", "Intra-country can add the country code.", "E.164 out"),
        ("Admin", "Simulator", "Test", "The article says the product has one.", "Use it before the carrier test"),
    ],
    [
        q("Custom number plans per site are capped at:", "200", ["5", "20", "5000"], "The article states 200."),
        q("Basic DID routing requires a custom number plan?", "No. DID routing is inherent.", ["Yes", "Only for toll-free", "Only in BYOC Premises"], "The article says plans are not required for that basic case."),
        q("988 on the default Suicide Prevention plan routes to:", "+18002738255", ["911", "A queue named Help", "The Home division"], "That destination is in the article. Confirm it before you rely on it."),
        q("Extension match is:", "Digit length, 4 to 6 digits, no normalization", ["Always E.164", "A bullseye ring", "An OAuth scope"], "The article describes that match type."),
        q("Intra-country normalization:", "Adds the site’s country code and produces E.164", ["Strips the plus", "Deletes the trunk", "Converts to an email"], "Inter-country and intra-country both normalize."),
        q("An E.164 number list entry:", "Keeps the plus and is not normalized", ["Must be 4 digits", "Must be 911", "Is always rewritten"], "The article says no normalization for that match type."),
    ],
    [("200", "Plans per site."), ("DID", "No custom plan required for basic routing."), ("988", "Default plan to +18002738255. Re-read before you depend on it."), ("Normalize", "Intra-country and inter-country. Not digit length.")],
    "Classify four strings",
    ["911.", "4501.", "+15555550100.", "A 10-digit national number.", "Say which ones normalize."],
    "Each string has a classification and a yes or no on normalization.",
    ("988 rewritten by a custom plan", "A custom regex plan matches 988 and sends it to a queue.", "Classification order put the custom plan ahead of Suicide Prevention.", "The default crisis route never runs.", "Remove the custom match and test 988 in the product call simulator."),
))

add(lesson(
    "b-monitor", "Watch the trunk, not only the flow", "Core", 11,
    "When audio fails and Architect Insights still shows runs, the trunk is the next object.",
    [
        "Monitor cloud media resources is the documented page for watching the cloud media your trunks use. A flow that transfers to ACD can be healthy while RTP is not. SIP responses tell you whether signaling completed. They do not tell you that the caller can hear the agent.",
        "Pair that page with the carrier’s view of the same call. If Genesys shows the trunk up and the carrier shows the INVITE rejected, you are looking at policy on the far end: ACL, TLS trust, or a number the carrier will not route. The DCVP migration exists because those far-end checks are easy to miss.",
    ],
    cites("media-mon", "byoc-overview", "dcvp", "rfc3261"),
    fig("Signaling can succeed while media is the thing you monitor.", [
        ("sip", "SIP 200", "trunk", 22, 28),
        ("mon", "Media monitor", "region", 55, 28),
        ("rtp", "RTP", "phone", 55, 70),
    ], [("sip", "mon"), ("mon", "rtp")]),
    "Split a failure into signaling or media",
    [
        ("Caller", "Trunk", "INVITE", "Look for a final response.", "RFC 3261"),
        ("Trunk", "Monitor", "Cloud media", "The documented Genesys view.", "Not a laptop capture alone"),
        ("Carrier", "ACL", "Drop or accept", "Far-end policy.", "DCVP ranges if you migrated"),
        ("Agent", "Ears", "One-way", "Signaling is not the proof.", "RTP is"),
    ],
    [
        q("A 200 OK proves the caller can hear the agent?", "No. It proves the SIP dialog, not RTP.", ["Yes", "Only with bullseye", "Only on CX 4"], "Media is a separate protocol."),
        q("The documented Genesys page for cloud media is:", "Monitor cloud media resources", ["The certification catalog", "The fair use table", "Flow Insights only"], "Use that page plus the carrier."),
        q("Flow Insights showing executions plus one-way audio means:", "Look at media, not at another publish", ["Rewrite the prompt", "Delete the queue", "Change the quiz"], "The flow ran. The audio path did not."),
        q("After a DCVP move, a carrier reject is often:", "ACL, trust, or ingress target", ["A wrap-up code", "A division rename", "A 7 day idle rule"], "Those are the article’s migration steps."),
        q("RFC 3261 is the citation for:", "The signaling dialog", ["The monitoring UI", "Utilization defaults", "Token counts"], "SIP, not the Genesys page."),
        q("Documentation address 192.0.2.10 in a lab trace is:", "A placeholder from RFC 5737, not your carrier", ["A Genesys anycast", "The US East API", "A queue id"], "Do not allow-list it as if it were production."),
    ],
    [("200 OK", "Dialog, not audio."), ("Monitor page", "Cloud media."), ("Far end", "ACL, CA, ingress."), ("Insights", "The flow can be innocent.")],
    "Triage one one-way call",
    ["Say what SIP proved.", "Name the Genesys page you would open.", "Name the carrier check.", "Say what you would not rewrite first."],
    "The first rewrite is not the Architect flow.",
    ("Flow blamed for RTP", "Three prompt edits did not restore audio.", "SIP: 200 OK. Carrier capture: RTP toward 203.0.113.10 blocked.", "203.0.113.0/24 in this lab is documentation space standing in for a discarded media range.", "Open the real media path with the carrier. Stop editing the prompt."),
))

add(lesson(
    "b-gcv", "Genesys Cloud Voice is the other door", "Core", 12,
    "If Genesys is the carrier, you buy numbers in a region that offers voice, and emergency is part of that product story rather than your trunk.",
    [
        "The Voice regions article lists where Genesys Cloud Voice operates and where it does not. Country tables restrict DID, toll-free, domestic, and international calling. FedRAMP is US-only for those services. The European Sovereign region does not extend its sovereignty promise to calls that leave the boundary.",
        "Choosing GCV does not delete a BYOC design you already have. It does mean you must not assume the GCV emergency record follows a BYOC number. The overview’s CX 1 voice features, including campaigns and callbacks, are available on either carrier model. The carrier model changes who you call when a number will not complete.",
    ],
    cites("gcv-regions", "emergency", "overview"),
    fig("Two carrier models, one org, different emergency owners.", [
        ("gcv", "GCV", "region", 22, 30),
        ("org", "Org", "queue", 50, 30),
        ("byoc", "BYOC", "trunk", 78, 30),
    ], [("gcv", "org"), ("byoc", "org")]),
    "Pick a model per number, not per slogan",
    [
        ("Buyer", "Region", "Voice offered?", "Read the Voice region table.", "Country row too"),
        ("Buyer", "GCV", "Genesys is the carrier", "Number purchase and emergency follow that product.", "Not a BYOC trunk"),
        ("Buyer", "BYOC", "You are the carrier’s customer", "You tell them the location.", "Genesys warning applies"),
        ("Admin", "Mix", "Both can exist", "Do not copy emergency data across.", "Test each number"),
    ],
    [
        q("Genesys Cloud Voice availability is documented in:", "Its own regions article, separate from the org deployment list", ["RFC 3261", "The queue article only", "AppFoundry"], "Use the Voice article."),
        q("FedRAMP voice services for other countries are:", "Unavailable, per the restrictions article", ["Worldwide", "EU only", "The same as Ireland"], "US services are the FedRAMP voice scope described there."),
        q("A BYOC number inherits GCV emergency registration automatically?", "No", ["Yes", "Only for 933", "Only on CX 4"], "The emergency article says the GCV information is not provided to the BYOC carrier."),
        q("Campaigns and callbacks in the CX 1 description require BYOC?", "No. They are voice features. The carrier model is a separate choice.", ["Yes", "They require a premises Edge", "They require predictive routing"], "Do not tie the feature list to one trunk type."),
        q("European Sovereign calls outside the boundary:", "Are not covered by the ESR sovereignty commitment", ["Are blocked by RFC", "Become free", "Use bullseye"], "The restrictions article says so."),
        q("The right person to open a ticket with when a BYOC number fails is:", "Your carrier, with Genesys if the trunk itself is down", ["Only the WFM team", "Only the certification vendor", "Nobody, it is RTP"], "You hold that contract."),
    ],
    [("GCV", "Genesys is the carrier. Read the region and country tables."), ("BYOC", "You are the carrier’s customer."), ("Emergency", "Does not cross over by itself."), ("Features", "CX voice features are not the same decision as the trunk.")],
    "Choose a model for two numbers",
    ["A US DID you want Genesys to provide.", "A carrier contract you must keep.", "Say who owns emergency for each.", "Name the article you would open for country coverage."],
    "Each number has an owner.",
    ("Sovereign surprise", "A number outside the ESR boundary was sold as fully sovereign.", "Destination country: outside the ESR list. Processing: non-EU carrier, per the restrictions article.", "The boundary was not read.", "Stop the claim, read the country table, and redesign the coverage."),
))

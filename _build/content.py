# -*- coding: utf-8 -*-
"""ARCOTRA site içeriği. Sayfalar buradan üretilir."""

SIRKET = {
    "ad": "ARCOTRA PRIVATE LIMITED",
    "kisa": "Arcotra",
    "wa": "https://wa.me/919289480963",
    "tel_goster": "+91 92894 80963",
    "mail": "info@arcotratrade.com",
    "adres_kisa": "Sector 63, Noida",
    "adres": ["A-64, 2nd &amp; 3rd Floor", "Sector 63, Noida", "Uttar Pradesh 201301, India"],
    "cin": "U74109UP2025PTC227082",
    "gstin": "09ABDCA2146E1Z0",
}

# ─────────────────────── ARCHITECTURE ───────────────────────
ARCH = [
 dict(slug="dream-house-design", num="01", ad="Dream House Design",
   gorsel="/img/panel-architecture-v2.jpg",
   kart="A house designed from the plot up: planned, drawn and shown in 3D before it is built.",
   basli="A house designed from the plot up.",
   giris="Most people come to us with a plot, a rough idea and a budget. We turn that into a "
         "buildable design: floor plans that work for how your family actually lives, elevations "
         "you can picture, and 3D views that let you walk through the house before a foundation "
         "is poured.",
   surec=[("Discovery","We start with the plot and the people. How many of you, how you live, "
           "what you liked and disliked about every home you have had."),
          ("Site &amp; requirements","Plot dimensions, orientation, access, local building rules, "
           "and the practical constraints that shape what is possible."),
          ("Concept","Two or three directions for the plan and the massing. We agree on one "
           "before any detail is drawn."),
          ("Design development","Floor plans, elevations, sections. Room by room, with real "
           "dimensions and real materials."),
          ("3D visualisation","Exterior and interior views. This is where most decisions get "
           "made, because you can finally see it."),
          ("Final proposal","Drawing set, material schedule and a package your builder can "
           "price and work from.")],
   hazir=("What helps us start","The more of this you have, the faster the first conversation goes. "
          "None of it is required to begin.",
          ["Plot location and dimensions","Number of floors","Bedrooms and bathrooms",
           "Who will live there","Architectural style you like","Approximate budget",
           "Desired timeline","Any local building restrictions"]),
   cta=("Start your house design","Send us the plot details and a few references. "
        "We will come back with what is possible on it.")),

 dict(slug="exterior-design", num="02", ad="Exterior House Design",
   gorsel="/img/photo-01.jpg",
   kart="Facades, elevations and the way a building meets the street, the light and the garden.",
   basli="Facades, elevations and how a building meets its plot.",
   giris="Sometimes the plan is already fixed: the house exists, or the layout is decided, and "
         "what needs work is the outside. Facade composition, materials, openings, roof line, "
         "and how the building sits in its plot.",
   surec=[("Discovery","What is already built or decided, and what you want the building to say."),
          ("Survey &amp; drawings","Existing elevations, photographs from every side, and the "
           "surrounding context."),
          ("Concept","Material palette and facade composition. Two directions, one chosen."),
          ("Design","Detailed elevations with materials, finishes and dimensions."),
          ("3D visualisation","Daylight and evening views, so you see the building as it will "
           "actually be seen."),
          ("Final proposal","Drawings and a material schedule ready for costing.")],
   hazir=("What helps us start","",
          ["Photographs from all sides","Existing plans or elevations","Plot orientation",
           "Materials available locally","Budget for the facade","References you like"]),
   cta=("Rework your facade","Send photographs of the building as it stands today.")),

 dict(slug="interior-design", num="03", ad="Room &amp; Interior Design",
   gorsel="/img/work-village-kitchen.jpg",
   kart="One room or the whole home: layout, materials, lighting and joinery, resolved in 3D.",
   basli="Start with one room, or design the whole home.",
   giris="Most people begin with the room that bothers them most, usually the kitchen. That is a "
         "perfectly good place to start. We plan the layout, choose materials and lighting, and "
         "build the room in three dimensions so you can change your mind while it is still free.",
   surec=[("Discovery","We understand what you want, and what is not working in the space today."),
          ("Requirements","Room dimensions, photographs, existing drawings, and what has to fit "
           "into the room."),
          ("Concept","Layout options and a material direction. We agree on one."),
          ("Design","Detailed design: joinery, finishes, lighting positions, dimensions."),
          ("3D visualisation","Realistic views of your own room. Change the worktop, move the "
           "island, try another colour."),
          ("Final proposal","Final visuals plus dimensioned drawings your carpenter or contractor "
           "can work from.")],
   hazir=("What helps us start","A phone photograph and a rough sketch with measurements is "
          "genuinely enough to begin.",
          ["Room type","Room dimensions","Photographs of the space","Existing drawings, if any",
           "Preferred style","Furniture that must fit","Material preferences","Budget range"]),
   cta=("Design your room","Send photographs and rough dimensions. A WhatsApp voice note works too.")),

 dict(slug="interior-visualisation", num="04", ad="Interior Visualisation",
   gorsel="/img/work-dyn-grocery.jpg",
   kart="Your design, your product, your space, rendered as it will look in use.",
   basli="Showing a space that does not exist yet.",
   giris="Sometimes the design is already settled and what is missing is the picture. A "
         "manufacturer needs their product shown in the shop it is sold for. A developer needs an "
         "apartment shown furnished. A designer needs their own scheme rendered properly. We build "
         "the space in 3D and light it so it reads as a photograph.",
   surec=[("Brief","What the images are for and who decides from them. A brochure image and a "
           "client approval image are framed differently."),
          ("What you send","Drawings, a sketch, product dimensions, or photographs of the real "
           "space. We work from whatever exists."),
          ("Materials &amp; setting","Finishes, lighting and the kind of room it belongs in. "
           "A shelving unit in a bakery is not the same picture as the same unit in a pharmacy."),
          ("Layout &amp; camera","We block out the scene and agree the views from a rough draft, "
           "before anything is lit."),
          ("Lighting &amp; dressing","The stage that decides whether it looks real. Light "
           "direction, reflections, and the objects that make a room look lived in."),
          ("Delivery","Full-resolution images plus one round of minor revisions.")],
   hazir=("What we need from you","",
          ["Product or room dimensions","Drawings or photographs","Material and finish details",
           "The setting it belongs in","Reference images you like","Number of views",
           "Output size and format","Whether text or branding goes on the image"]),
   bilgi=[("Retail and product","A shelving manufacturer&rsquo;s range shown stocked and lit in "
           "the shop it is sold for. An empty steel frame tells a buyer nothing; a full aisle "
           "tells them everything."),
          ("Residential interiors","Apartments and houses shown furnished, so a buyer can picture "
           "living there before the plaster is dry."),
          ("Material options","The same room rendered with two worktops or three floor finishes, "
           "so the decision is made on screen instead of after the joinery is built."),
          ("Output","Still images at print or web resolution, in the aspect ratio you need for "
           "catalogues, listings or presentations.")],
   cta=("Get your space visualised","Send the product or the drawings and tell us where it belongs.")),

 dict(slug="3d-visualisation", num="05", ad="3D Visualisation",
   gorsel="/img/kitchen-option-stone.jpg",
   kart="Buildings rendered from architectural drawings, for approvals, investors or sales.",
   basli="Buildings, rendered from architectural drawings.",
   giris="Architectural renders: the building seen from outside, in its setting, at the hour that "
         "shows it best. Developers use them to sell before a foundation is poured, architects to "
         "present, planning committees to decide. For interiors and products in a space, see "
         "Interior Visualisation.",
   surec=[("Brief","What the images are for, and who will look at them. A sales render and a "
           "decision render are not the same picture."),
          ("Drawings &amp; references","Plans, elevations or a model, plus reference images for "
           "the mood you want."),
          ("Materials","We agree the finishes before modelling, because changing them later costs "
           "time."),
          ("Camera views","We propose the views and you confirm them from a rough draft, not from "
           "a finished image."),
          ("Draft render","Low-resolution passes for composition and light. Changes are cheap here."),
          ("Final delivery","Full-resolution images, plus one round of minor revisions.")],
   hazir=("What we need from you","",
          ["Architectural drawings or a 3D model","Accurate dimensions","Reference images",
           "Material and finish list","Which views you want","How many views","Output resolution",
           "Revision expectations"]),
   cta=("Get your project visualised","Send the drawings and tell us how many views you need.")),

 dict(slug="architectural-design", num="06", ad="Architectural Design",
   gorsel="/img/cons-drawing.jpg",
   kart="Full architectural service for buildings beyond a single home, concept to drawing set.",
   basli="Apartment buildings, hostels, academies and commercial premises.",
   giris="Apartment buildings, hostels, academies, commercial premises. Projects where the plan has "
         "to satisfy regulations, budgets and dozens of people at once, and where the drawing set "
         "is the thing that gets built from.",
   surec=[("Discovery","Purpose of the building, who uses it, and the commercial or institutional "
           "constraints behind it."),
          ("Site &amp; regulations","Plot, orientation, access, setbacks, coverage and the rules "
           "that apply."),
          ("Concept","Massing and plan strategy. Circulation and daylight decided early, because "
           "they cannot be fixed later."),
          ("Design development","Full plans, sections and elevations, coordinated room by room."),
          ("3D visualisation","Views for approvals, investors or marketing."),
          ("Drawing set","A coordinated set your engineers and contractor can build from.")],
   hazir=("What helps us start","",
          ["Plot documents and dimensions","Building type and intended use","Required areas or "
           "unit count","Applicable regulations","Budget range","Programme and timeline"]),
   cta=("Discuss your project","Tell us the building type, the plot and the timeline.")),
]

# ─────────────────────── CONSTRUCTION ───────────────────────
CONS = [
 dict(slug="residential-construction", num="01", ad="Residential Construction",
   gorsel="/img/panel-construction-v2.jpg",
   kart="Houses and apartments built to the drawings, costed and scheduled.",
   basli="Houses and apartments, built to the drawings.",
   giris="Building a home is where most budgets slip and most timelines break. We take the "
         "drawings — ours or someone else&rsquo;s — and turn them into a costed programme, then "
         "run the work against it.",
   surec=[("Consultation","What is being built, where, and to whose drawings."),
          ("Site assessment","Access for machinery and deliveries, ground conditions, water and "
           "power. These decide the sequence more than the design does."),
          ("Programme","Trades booked in order, with the weather-dependent work placed where the "
           "season allows it."),
          ("Cost plan","Priced by stage: substructure, frame, envelope, services, finishes. "
           "So you can see what each part costs before it starts."),
          ("Structure &amp; envelope","Foundations, frame, roof and openings. The stage where "
           "corrections are still cheap."),
          ("Services &amp; finishes","Plumbing and electrical first fix, then plaster, joinery "
           "and final fittings."),
          ("Handover","Snagging list worked through, completion certificate, and the warranties "
           "and drawings you will need when something needs fixing in five years.")],
   hazir=("What helps us quote","",
          ["Plot location","Drawings, if you have them","Built-up area","Number of floors",
           "Level of finish expected","Target start date","Budget range"]),
   cta=("Request a quotation","Send the drawings and the plot location for a costed estimate.")),

 dict(slug="commercial-construction", num="02", ad="Commercial Construction",
   gorsel="/img/photo-08.jpg",
   kart="Offices, retail and institutional buildings, delivered against a programme.",
   basli="Offices, retail and institutional premises, delivered on a date.",
   giris="A shop that opens late loses a season. An office handed over late costs rent on two "
         "buildings. Commercial construction is less about craft and more about sequence, and "
         "that is how we plan it.",
   surec=[("Consultation","Use, floor area, and the date the premises has to be trading."),
          ("Constraints survey","Existing structure or bare plot, incoming services, delivery "
           "access and permitted working hours. In an occupied building the last one governs "
           "everything."),
          ("Critical path","The sequence agreed before work starts, with the items that cannot "
           "slip identified and dated."),
          ("Package pricing","Priced by trade package, with provisional sums marked as provisional "
           "rather than buried in a total."),
          ("Fit-out","Built in the agreed sequence, with progress measured against the programme "
           "each week."),
          ("Compliance &amp; testing","Fire, electrical and access requirements tested and "
           "certified. This is the paperwork that decides whether you can legally open."),
          ("Handover","Completion, operation and maintenance documents, and a defect period.")],
   hazir=("What helps us quote","",
          ["Type of premises","Floor area","Location","Drawings or a fit-out brief",
           "Required completion date","Operating constraints","Budget range"]),
   cta=("Request a quotation","Tell us the premises, the area and the date it must open.")),

 dict(slug="renovation", num="03", ad="Renovation",
   gorsel="/img/photo-01.jpg",
   kart="Old houses, tired flats and buildings that need to work differently than they do now.",
   basli="Renovation is design before it is demolition.",
   giris="Old buildings hide things. The drawings are wrong, walls are not where they should be, "
         "and something structural is always where you wanted an opening. We design the change "
         "first, then carry it out, so surprises are answered on paper, not by three people "
         "standing in the dust.",
   surec=[("Consultation","What the building does now, and what you need it to do instead."),
          ("Measured survey","We measure what is there today rather than trusting the old plans. "
           "In an old building the two rarely match."),
          ("Opening up","Where the drawings are uncertain we open a small area first: a ceiling "
           "void, a wall base. Nothing is priced on a guess."),
          ("Structural check","Which walls carry load, where beams are needed, and what that does "
           "to the layout you wanted."),
          ("Costing","Priced by stage, with a stated contingency for what old buildings hide. "
           "A renovation quoted without one is a quote that will change."),
          ("Sequencing","Demolition, structure, services, then finishes. Getting this order wrong "
           "is what makes renovations run long."),
          ("Execution &amp; handover","The work itself, with checks before each stage is covered over, "
           "and a record of what was built.")],
   hazir=("What helps us quote","",
          ["Property type and age","Photographs of every room","Existing plans, if any",
           "What you want changed","Whether you will live there during the work",
           "Budget range","Target start date"]),
   cta=("Request a site consultation","Send photographs of the space as it stands today.")),

 dict(slug="project-management", num="04", ad="Project Management",
   gorsel="/img/cons-drawing.jpg",
   kart="You hold the contracts; we run the programme, the trades and the quality on your behalf.",
   basli="We run the programme; you keep the contracts.",
   giris="Some clients want to keep their own contractors and their own contracts, but need "
         "someone whose full-time job is the programme, the sequence and the standard of work. "
         "That is this service. You stay in control of the money; we make sure the work matches "
         "the drawings.",
   surec=[("Review","We read the drawings, the contracts and the programme you already have, "
           "and tell you where the exposure sits."),
          ("Baseline programme","A schedule with the critical path marked, so it is visible which "
           "delays matter and which do not."),
          ("Cost plan","Budget mapped to stages. You see a variance the week it appears, not at "
           "the end of the quarter."),
          ("Site oversight","Regular visits, trade coordination, and every instruction issued in "
           "writing so nobody can claim they were told otherwise."),
          ("Stage inspection","Work checked against drawings and specification before it is "
           "covered, signed off stage by stage."),
          ("Reporting","A short written report on progress, cost and risk, at an interval you set."),
          ("Closing out","Snagging list tracked to completion, warranties and documents collected.")],
   hazir=("What helps us start","",
          ["Project type and location","Current stage","Drawings and specifications",
           "Contractors already appointed","Budget and programme","Where you feel the risk is"]),
   cta=("Discuss project management","Tell us where the project stands today.")),

 dict(slug="turnkey-projects", num="05", ad="Turnkey Projects",
   gorsel="/img/cons-bedroom.jpg",
   kart="Design, build and finish under one contract. You hand over a plot and receive a building.",
   basli="One contract, one point of responsibility.",
   giris="Turnkey means you deal with us and we deal with everyone else. Design, approvals, "
         "construction, finishes and handover under a single agreement, priced up front, with "
         "one party accountable when something goes wrong.",
   surec=[("Brief","What you want built, where, to what standard, and by when."),
          ("Feasibility","Plot, regulations, services and budget checked together. If the three "
           "do not meet, we say so before you spend on design."),
          ("Design","Full design developed and signed off. Under a turnkey contract the price "
           "follows the design, so the design is fixed first."),
          ("Fixed proposal","One price covering design, approvals, construction and finishes, "
           "with the specification attached to it."),
          ("Single contract","One agreement, one party accountable. You will not be arbitrating "
           "between an architect and a contractor when something goes wrong."),
          ("Construction","Built and managed by us, reported against the programme."),
          ("Handover","A finished building, documentation, and a defect period during which we "
           "come back.")],
   hazir=("What helps us quote","",
          ["Plot location and size","Building type and use","Required area","Level of finish",
           "Target completion date","Budget range","Whether design already exists"]),
   cta=("Request a turnkey proposal","Tell us the plot, the building and the date you need it.")),
]

# ─────────────────────── TRADE ───────────────────────
MERMER = [
 ("makrana-white","Makrana White","Rajasthan","The stone the Taj Mahal was built from. Dense, bright white, takes a high polish."),
 ("banswara-white","Banswara White","Rajasthan","Warm off-white with soft grey movement. A quieter alternative to pure white."),
 ("statuario-india","Statuario India","Rajasthan","White ground with bold grey veining. Statement worktops and vanities."),
 ("katni-grey","Katni Grey","Madhya Pradesh","Even mid-grey with fine veining. Forgiving underfoot and easy to match."),
 ("fantasy-brown","Fantasy Brown","Rajasthan","Banded brown and grey with strong movement. No two slabs alike."),
 ("emperador-brown","Emperador Brown","Rajasthan","Deep brown with a fine white web. Warm in low light."),
 ("gujarat-green","Gujarat Green","Gujarat","Dark green with white veining. Cladding, reception desks, feature walls."),
 ("black-marquina","Black Marquina","Rajasthan","Near-black with sharp white veins. High contrast, high polish."),
 ("pink-marble","Pink Marble","Rajasthan","Soft rose with pale veining. Long used in Indian architecture."),
 ("agra-red","Agra Red","Uttar Pradesh","Deep red sandstone-toned marble. Traditional in north Indian building."),
]
SERAMIK = [
 ("vitrified-tiles","Vitrified Tiles","High gloss","Low porosity, hard wearing. The volume floor product for large areas."),
 ("glazed-porcelain","Glazed Porcelain","Natural finish","Glazed surface over a porcelain body. Wide range of looks."),
 ("full-body-tiles","Full Body Tiles","Through-colour","Colour runs through the tile, so chips and edges do not show."),
 ("matt-finish-tiles","Matt Finish Tiles","Non-reflective","Less glare, better grip. Bathrooms and busy floors."),
 ("large-format-tiles","Large Format Tiles","Fewer joints","Big panels for floors and cladding. Fewer grout lines to clean."),
 ("wooden-look-tiles","Wooden Look Tiles","Plank format","The look of timber with the wear resistance of porcelain."),
 ("concrete-look","Concrete Look","Contemporary","Flat mineral tone. Popular in commercial and modern residential."),
 ("wall-tiles","Wall Tiles","Marble effect","Lightweight wall formats, including book-matched marble prints."),
 ("3d-tiles","3D Tiles","Relief surface","Textured relief panels for feature walls and headboard walls."),
 ("decorative-tiles","Decorative Tiles","Patterned","Printed and encaustic-style patterns for floors and splashbacks."),
]

TRADE = [
 dict(slug="marble", num="01", ad="Marble",
   gorsel="/img/products/statuario-india.jpg",
   kart="Ten Indian marbles, quarried in Rajasthan, Madhya Pradesh, Gujarat and Uttar Pradesh.",
   basli="Ten Indian marbles, block to slab.",
   giris="India is one of the largest producers of natural stone on earth. We supply marble by the "
         "container — selected at the block, cut to your specification, crated and shipped.",
   urunler=("Available marbles", MERMER),
   bilgi=[("Formats","Slabs, cut-to-size tiles, stair treads, risers and skirting."),
          ("Finishes","Polished, honed, leathered and brushed."),
          ("Thickness","16 mm and 18 mm standard; 20 mm and 30 mm on request."),
          ("Selection","Photographs of the actual lot before cutting. Stone varies within a seam, "
           "so the block matters as much as the name."),
          ("Supply","Project quantities and repeat commercial supply, not single-slab retail."),
          ("Export","Crating, export documentation and freight from an Indian port.")],
   cta=("Request a marble quotation","Tell us the marble, the area and the format. "
        "A reference photograph is the fastest way to start.")),

 dict(slug="granite-natural-stone", num="02", ad="Granite &amp; Natural Stone",
   gorsel="/img/trade-quarry.jpg",
   kart="Granite, sandstone and quartzite for surfaces that take heavy wear.",
   basli="Granite, sandstone and quartzite for heavy-wear surfaces.",
   giris="Granite and the harder Indian stones go where marble should not: kitchen worktops in "
         "commercial use, external paving, stair treads in public buildings, and cladding that "
         "has to survive weather without sealing every year.",
   bilgi=[("Materials","Granite, sandstone, quartzite and limestone."),
          ("Formats","Slabs, cut-to-size, paving, kerbs and cladding panels."),
          ("Finishes","Polished, flamed, honed, bush-hammered and sandblasted."),
          ("Typical uses","Worktops, external paving, facades, stair treads and landscaping."),
          ("Why granite","Harder and less porous than marble. Higher resistance to acids, "
           "abrasion and frost."),
          ("Export","Crated on timber pallets, containerised, documented for export.")],
   cta=("Request a stone quotation","Tell us the application — that decides the material "
        "more than the colour does.")),

 dict(slug="ceramic-porcelain", num="03", ad="Ceramic &amp; Porcelain",
   gorsel="/img/products/large-format-tiles.jpg",
   kart="Ten tile ranges made in India: floor, wall and large-format porcelain.",
   basli="Ten Indian tile ranges, supplied by the container.",
   giris="India&rsquo;s ceramic industry ships to every continent, and the price-to-quality ratio "
         "at volume is difficult to match. We supply full containers across the finishes that "
         "actually move.",
   urunler=("Available ranges", SERAMIK),
   bilgi=[("Formats","From 300×300 mm up to 1200×2400 mm large-format panels."),
          ("Finishes","Gloss, matt, satin, textured and anti-skid."),
          ("Grades","Standard and premium grade, clearly quoted as such."),
          ("Packing","Cartons on shrink-wrapped pallets, container-loaded."),
          ("Samples","Sample tiles before a volume order. Batches vary; shade and calibre are "
           "matched per order."),
          ("Export","Full container loads, export documentation included.")],
   cta=("Request a tile quotation","Tell us the finish, the size and the square metres.")),

 dict(slug="sanitary-building-materials", num="04", ad="Sanitary &amp; Building Materials",
   gorsel="/img/photo-07.jpg",
   kart="Sanitaryware, fittings and finishing materials, consolidated into the same shipment.",
   basli="Sanitaryware and finishing materials, in the same shipment.",
   giris="A project that needs marble usually needs the rest of the bathroom too. Rather than "
         "running three suppliers and three shipments, we consolidate sanitaryware and finishing "
         "materials into the same container.",
   bilgi=[("Sanitaryware","Basins, water closets, pedestals and counter tops."),
          ("Fittings","Taps, showers, and bathroom accessories."),
          ("Finishing materials","Adhesives, grouts and installation consumables."),
          ("Why consolidate","One shipment, one set of documents, one freight cost, instead of "
           "three of each."),
          ("Sourcing","Specified against the project, not picked from whatever is in stock."),
          ("Export","Combined loading with stone or tile in the same container.")],
   cta=("Ask about consolidated supply","Send the project schedule and we will quote it as one "
        "shipment.")),

 dict(slug="sourcing-from-india", num="05", ad="Sourcing from India",
   gorsel="/img/trade-interior.jpg",
   kart="You know what you want; we find it, check it and get it priced properly.",
   basli="You send a reference; we find it, check it and price it.",
   giris="We design interiors as well as supply them. That means when you send a reference image, "
         "we are reading it the way a designer does — not matching a colour swatch and hoping the "
         "material behaves the same way in the room.",
   bilgi=[("How it starts","A reference photograph, a specification, or a sample you already have."),
          ("What we do","Identify the material, find producers, verify quality and come back with "
           "options and prices."),
          ("Verification","Physical inspection before shipment. Photographs of the actual lot, "
           "not a catalogue image."),
          ("Honest advice","If what you are asking for is the wrong material for the use, we will "
           "say so before you order it."),
          ("Consolidation","Multiple materials from multiple producers, combined into one shipment."),
          ("Documentation","Invoiced from a GST-registered Indian company, with full export papers.")],
   cta=("Send us a reference","A photograph and a rough quantity is enough to start.")),

 dict(slug="global-export", num="06", ad="Global Export",
   gorsel="/img/panel-trade-v2.jpg",
   kart="Crating, documentation and freight from an Indian port to your project.",
   basli="Crating, documentation and freight from an Indian port.",
   giris="Getting stone out of India is a paperwork exercise as much as a logistics one. We handle "
         "the part between the factory gate and your site, so what arrives matches what you ordered "
         "and clears customs without a phone call at midnight.",
   bilgi=[("Packing","Timber crates and pallets, built for stone weight and sea transit."),
          ("Loading","Full container load (FCL); part loads consolidated where volumes allow."),
          ("Terms","FOB and CIF quoted; other Incoterms on request."),
          ("Documentation","Commercial invoice, packing list, bill of lading, certificate of "
           "origin and any inspection certificates required."),
          ("Ports","Shipped from Indian ports including Mundra, Nhava Sheva and Kandla."),
          ("Company","ARCOTRA PRIVATE LIMITED. GST-registered, exporting under LUT.")],
   cta=("Ask about shipping","Tell us the destination port and the volume for a freight estimate.")),
]

BOLUMLER = [
 dict(slug="architecture", num="01", ad="Architecture",
   gorsel="/img/panel-architecture-v2.jpg",
   kart="Homes, interiors and buildings designed in 3D, so you see the space before it is built.",
   basli="Design that is decided on screen, not on site.",
   giris="From a single room to a whole building. We plan it, draw it and show it to you in three "
         "dimensions &mdash; because every decision made before construction starts is a decision "
         "that costs nothing to change.",
   hizmetler=ARCH),
 dict(slug="construction", num="02", ad="Construction",
   gorsel="/img/panel-construction-v2.jpg",
   kart="Residential, commercial and renovation work &mdash; costed, scheduled and delivered.",
   basli="Built to the drawings, against a programme.",
   giris="New build, renovation and turnkey delivery. The drawings tell you what it should be; the "
         "programme and the cost plan tell you whether it will actually happen that way.",
   hizmetler=CONS),
 dict(slug="trade", num="03", ad="Trade",
   gorsel="/img/panel-trade-v2.jpg",
   kart="Marble, natural stone, ceramic and building materials, shipped from India by the container.",
   basli="Marble, stone, ceramic and building materials from India.",
   giris="We supply the stone and tile that finishes buildings &mdash; and because we draw those "
         "buildings too, what we recommend comes from having designed the room, not from "
         "what is sitting in a warehouse.",
   hizmetler=TRADE),
]

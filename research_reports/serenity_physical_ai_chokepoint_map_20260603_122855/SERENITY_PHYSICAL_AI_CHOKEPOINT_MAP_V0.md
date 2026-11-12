# SERENITY_PHYSICAL_AI_CHOKEPOINT_MAP_V0

Generated: 20260603_122855
Project: Serenity Alpha Research
Mode: research-only, public-evidence synthesis, no brokerage access, no secrets, no scheduler/cron/service/monitor.

## 1. Executive Summary

Physical AI is not at one stage. Industrial robots and warehouse automation are already real physical systems with installed bases, repeat deployments, safety standards, and in some cases revenue/backlog proof. Humanoid robotics is earlier: there are real pilots and early deployments, but broad commercial adoption is not yet proven by revenue, margins, service economics, or large repeat fleets.

Where it is real:
- Industrial robotics: Confirmed by IFR data showing 4.664 million industrial robots in operational use worldwide in 2024 and 2024 as the second-highest annual installation count.
- Warehouse automation: Confirmed by Amazon's disclosed robotics fleet scale and by public warehouse automation filings/backlog in selected vendors.
- Constrained manipulation: Confirmed in selected workflows such as warehouse sortation, package handling, picking/stowing subsets, machine tending and inspection.

Where it is still hype:
- General-purpose humanoid robots replacing broad human labor across homes and factories.
- Robotics videos that show one task but omit uptime, exception rate, safety case, deployment cost and maintenance burden.
- Partner logos, conference demos and model releases treated as commercial adoption.
- Battery or world-model narratives that are not tied to robot shipments, repeat customers or measurable productivity.

Why this differs from AI datacenter infrastructure:
- Datacenter AI scales by building dense, standardized compute clusters. Physical AI scales by moving atoms in irregular sites: joints wear out, batteries heat, grippers miss, sensors drift, safety standards apply, and field service matters.
- The chokepoint is not only compute. It is the conversion of intelligence into reliable, safe, maintainable physical work.
- The strongest research lane is therefore not 'robots are coming'; it is 'which physical layer breaks when robots move from demo to fleet deployment?'

## 2. Physical AI System Map


| System block | What it does | Current stage | Bottleneck read |
|---|---|---|---|
| Perception | Cameras, depth, tactile and force sensing convert the world into state. | Real in constrained industrial/warehouse workflows; early for general humanoids. | Reliability under messy lighting, SKU variance, occlusion and contact. |
| Compute | On-robot edge inference and local planning. | Product platforms exist; fleet-scale revenue linkage is less visible. | Power/thermal envelope, deterministic latency, software compatibility. |
| Control | Converts plans into safe, synchronized motion. | Mature in industrial arms; harder for dynamic mobile manipulators. | Functional safety, real-time buses, fallback behavior, cybersecurity. |
| Motion | Motors, reducers, actuators and joints produce torque. | Very real for industrial robots; humanoid-specific volume still early. | Precision reducers, torque density, wear, heat, backlash and qualification. |
| Power | Battery, BMS, power electronics and charging. | Real for AMR fleets; humanoid miracle narratives are weak. | Runtime, safety certification, pack integration, thermal runaway mitigation. |
| End effector / manipulation | Grippers, suction, hands and tooling interact with objects. | Real in narrow pick/stow tasks; early for broad dexterity. | Exception rate, force/tactile feedback, object diversity. |
| Software / simulation | VLA models, world models, synthetic data, digital twins. | Rapid model progress, but mostly E1-E2 unless tied to deployments. | Sim-to-real transfer, validation and customer economics. |
| Data collection | Real robot trajectories, human demos, fleet logs, QA data. | Scarce and fragmented. | Physical data quality, privacy/safety controls, task diversity. |
| Manufacturing | Builds robots, joints, sensors and automation cells. | Mature for industrial robots; early for humanoid mass production. | Qualified suppliers, yield, repairability and capex discipline. |
| Deployment / maintenance | Site survey, safety certification, installation, field service. | Very real and underappreciated. | Skilled labor, uptime, spares, safety standards and customer ROI. |


## 3. Supply-Chain Stack

1. **Physical AI application** -> Humanoid robotics, industrial robotics, warehouse automation, edge AI inspection, machine tending | constraint: Demand / adoption / workflow fit | evidence: E2-E5 depending on use case
2. **Robot platform / system integrator** -> AMRs, arms, humanoid platforms, end-to-end warehouse automation cells | constraint: Manufacturing, field service, integration | evidence: E2-E4
3. **Edge compute / local inference** -> Robot brain, onboard GPU/accelerator, real-time inference stack | constraint: Compute availability, power envelope, software compatibility | evidence: E2-E3
4. **Perception sensors / machine vision** -> Cameras, depth sensors, force/torque, tactile sensing, industrial vision | constraint: Accuracy / reliability / calibration | evidence: E3-E4 in factories and warehouses; E1-E2 in humanoid dexterity
5. **Actuators / motors / reducers** -> Servo motors, drives, precision reducers, harmonic/cycloidal/RV gears, integrated joints | constraint: Precision mechanical capacity and qualification | evidence: E3-E4 for industrial robots; E1-E2 for humanoid-specific joints
6. **Control electronics / motion control** -> MCUs, servo drives, safety controllers, PLC/robot controllers, real-time bus | constraint: Safety certification and deterministic latency | evidence: E3-E4 in industrial; E1-E2 in general humanoids
7. **Power / batteries / thermal ruggedization** -> Battery packs, BMS, power electronics, cooling, rugged enclosures | constraint: Energy density, BMS safety, heat rejection | evidence: E2-E3 for mobile robots; E0-E1 for miracle battery narratives
8. **Software / simulation / data / world models** -> VLA models, world models, digital twins, synthetic data, fleet learning, MLOps | constraint: Qualification and validation, not only model quality | evidence: E1-E2 mostly; E3 only if tied to production deployment
9. **Testing / deployment / maintenance** -> Robot safety validation, QA, calibration, maintenance, spare parts, deployment engineering | constraint: Field service and safety certification capacity | evidence: E3-E5 in mature automation; E1-E2 in humanoids

## 4. Bottleneck Candidates By Layer


### 1. Testing / deployment / maintenance - Safety-certified deployment, uptime, integration and maintenance capacity
- Why bottleneck: Physical AI fails commercially if robots cannot be installed, certified, maintained and kept productive in messy sites. Scaling from one demo to hundreds of workcells turns the bottleneck into deployment engineering, safety validation, field service and spare parts.
- Supply-constrained: Yes: skilled integrators, safety engineers, field technicians and validation capacity do not scale like software downloads.
- Technical barriers: High: functional safety, calibration, failure handling, cybersecurity, human-robot interaction, uptime analytics.
- Customer urgency: High in warehouses/factories where labor availability, ergonomics and throughput already matter; lower in general humanoid use cases.
- Pricing power: Medium to high if vendors own certified workflows and service loops; lower for commodity integration.
- Later public-company investability: Yes later through automation integrators, controls vendors, warehouse automation vendors, industrial safety/testing suppliers.
- Likely hype: Low: this is a real deployment constraint, not a demo narrative.
- Evidence ladder: E3-E5 for mature industrial/warehouse automation; E1-E2 for humanoids.
- Evidence class: Confirmed for industrial/warehouse automation; Inferred for humanoid scaling.
- Serenity-style fit: Strong Serenity fit: dull, underfollowed, physical, customer-facing, and likely to reveal small/mid-cap suppliers after evidence mapping.
- Must be proven before company mapping: Named repeat deployments, service revenue, backlog tied to installations, uptime metrics, safety certifications, repeat customers.

### 2. Actuators / motors / reducers - High-reliability motion stack: precision reducers, integrated joints, servo drives and thermal durability
- Why bottleneck: Every mobile manipulator or humanoid converts intelligence into torque. Joints need compact high-torque actuation, low backlash, shock tolerance, long duty cycles and safe failure modes. If deployment 10x, joint qualification and durable actuator supply can break before software ambition.
- Supply-constrained: Likely yes in high-end reducers and qualified integrated joints; commodity motors less constrained.
- Technical barriers: Very high: torque density, backlash, overload resistance, lubrication, wear, heat, safety stops.
- Customer urgency: High for industrial robots; medium for humanoids until orders move from pilots to fleet deployments.
- Pricing power: Potentially high where supplier concentration and qualification lock-in exist.
- Later public-company investability: Yes later through precision reducer, servo, drive, and motion-control suppliers.
- Likely hype: Medium: the physical need is real, but humanoid volume assumptions are often speculative.
- Evidence ladder: E3-E4 industrial; E1-E2 humanoid.
- Evidence class: Confirmed for industrial robot reducers; Inferred for humanoid-specific ramp.
- Serenity-style fit: Strong Serenity fit if supplier concentration, qualification cycles and backlog conversion are shown.
- Must be proven before company mapping: Reducer/servo order growth, capacity expansion, named OEM design-ins, shipment volume, margin resilience, failure-rate data.

### 3. Perception / end effector / manipulation - Reliable perception and manipulation across SKU/object variance
- Why bottleneck: Warehouses and factories are not clean benchmark datasets. Lighting, packaging, reflective surfaces, deformable objects, occlusion and force control make pick/stow/manipulation hard. A robot that handles a subset of SKUs still needs human fallback.
- Supply-constrained: Partly: specialized sensors and end effectors are available, but robust application-specific integration is constrained.
- Technical barriers: High: tactile sensing, force control, computer vision, grasp planning, suction/finger tooling, failure detection.
- Customer urgency: High in logistics picking/stowing and inspection; medium elsewhere.
- Pricing power: Medium to high where tools improve throughput or reduce human exceptions.
- Later public-company investability: Yes through machine vision, sensors, end-of-arm tooling, industrial software and automation vendors.
- Likely hype: Medium: demos overstate generality if they omit exception rates and human fallback.
- Evidence ladder: E3-E4 for selected warehouse/industrial workflows; E1-E2 for general dexterity.
- Evidence class: Confirmed for constrained workflows; Inferred for generalized manipulation.
- Serenity-style fit: Medium-to-strong Serenity fit after mapping repeat deployments and exception economics.
- Must be proven before company mapping: Repeat customer deployment, SKU coverage, exception rate, speed vs human baseline, uptime, service margin.

### 4. Edge compute / power / thermal co-design - On-robot inference under power, latency and heat constraints
- Why bottleneck: Physical AI needs perception, planning and control at low latency without relying entirely on cloud connectivity. More capable VLA/world models increase compute demand, but mobile robots have tight power and thermal budgets.
- Supply-constrained: Compute supply can be concentrated; integration of compute, sensors, power and thermal is the harder constraint.
- Technical barriers: High: real-time inference, memory bandwidth, sensor ingest, deterministic latency, power envelope, thermal throttling.
- Customer urgency: High for autonomous mobile robots and humanoids; lower for fixed industrial arms with tethered compute.
- Pricing power: High for leading modules; medium for downstream integrators.
- Later public-company investability: Yes through edge AI module suppliers, industrial edge compute, sensor bridge, power/thermal vendors.
- Likely hype: Medium: dev-kit availability is not the same as fleet revenue.
- Evidence ladder: E2-E3.
- Evidence class: Confirmed for product availability; Management claim / Inferred for scale adoption.
- Serenity-style fit: Medium Serenity fit; likely crowded at the obvious compute leader, better in second-order power/sensor/thermal suppliers if proven.
- Must be proven before company mapping: Production module attach rates, OEM design wins converting to shipment volume, thermal field data, revenue contribution.

### 5. Warehouse automation platform economics - Capex-heavy automation systems with real backlog but customer concentration and installation throughput risk
- Why bottleneck: Warehouse automation is one of the few Physical AI areas with real revenue/backlog proof. The bottleneck is less the robot demo and more system installation cadence, customer concentration, site readiness and ROI.
- Supply-constrained: Yes for deployment throughput and large-scale systems integration.
- Technical barriers: Medium to high: systems software, controls, mobile robots, sequencing, installation.
- Customer urgency: High where customers have clear throughput/labor/fulfillment ROI.
- Pricing power: Medium: strong if ROI is proven, weaker if capex cycles slow.
- Later public-company investability: Yes through warehouse automation vendors, AMR suppliers, controls, machine vision and integrators.
- Likely hype: Low to medium: real revenue exists, but concentration can create misleading backlog quality.
- Evidence ladder: E4-E5 for leading warehouse automation; E2-E3 for newer humanoid add-ons.
- Evidence class: Confirmed for selected warehouse automation; Inferred for broader Physical AI expansion.
- Serenity-style fit: Medium Serenity fit; better for supplier mapping than for obvious platform names.
- Must be proven before company mapping: Multi-customer backlog, installations per quarter, cash conversion, service attachment, reduced customer concentration.

### 6. Simulation / synthetic data / world models - Robot data scarcity and sim-to-real validation
- Why bottleneck: Robots need far more real-world physical interaction data than internet-trained models. Simulation and synthetic data can accelerate training, but the bottleneck is validated transfer to real production tasks.
- Supply-constrained: Software capacity is less supply-constrained; high-quality task data and validation environments are constrained.
- Technical barriers: High: physics fidelity, contact modeling, domain randomization, policy validation, safety filters.
- Customer urgency: High for model builders; less direct urgency for end customers until it lowers deployment cost.
- Pricing power: Unclear: platform value may be high, but monetization path is early.
- Later public-company investability: Yes later through simulation platforms, robotics software, digital twins and data infrastructure.
- Likely hype: High if not tied to real deployment improvement.
- Evidence ladder: E1-E2 today unless connected to named customer production results.
- Evidence class: Management claim / Inferred.
- Serenity-style fit: Early but promising; not strong enough alone for Serenity-style supplier hunt until revenue linkage appears.
- Must be proven before company mapping: Real-world task success improvement, named customer deployment, reduced training time, reduced exception rate, paid production contracts.

### 7. Power / batteries - Runtime and battery safety for mobile manipulators and humanoids
- Why bottleneck: Mobile robots need enough runtime and safety to justify deployment, but battery improvements are incremental and often not the decisive chokepoint compared with actuation, safety and integration.
- Supply-constrained: Mostly no for commodity lithium packs; yes for certified packs/BMS in harsh industrial settings.
- Technical barriers: Medium: BMS, safety certification, thermal runaway mitigation, charging cycles, pack integration.
- Customer urgency: Medium; high only where runtime prevents task completion or safety certification blocks deployment.
- Pricing power: Low to medium unless a supplier owns certified rugged packs with validated reliability.
- Later public-company investability: Possible through BMS, power electronics, battery pack and industrial charging suppliers.
- Likely hype: High when framed as solid-state battery miracle or humanoid adoption linchpin without deployment evidence.
- Evidence ladder: E0-E2 for humanoid battery miracle claims; E3 for certified AMR battery systems.
- Evidence class: Inferred / Weak depending on claim.
- Serenity-style fit: Medium only after certification and deployment data; no-go if thesis depends on chemistry speculation.
- Must be proven before company mapping: Certified pack adoption, field failure data, runtime economics, replacement cycles, customer maintenance economics.


## 5. Evidence Ladder

Evidence labels used:
- E0: narrative only.
- E1: demo / prototype.
- E2: pilot / early deployment.
- E3: named customer / repeat deployment.
- E4: revenue or backlog contribution.
- E5: scale production / margin / cash-flow proof.

Claim classes:
- Confirmed: official filing, company disclosure, standard body or directly documented deployment.
- Management claims: company-provided claims that may be accurate but require outside validation.
- Inference: cross-source synthesis from public evidence.
- Speculation: plausible but not proven; not used as a hard conclusion.

Strongest evidence lines:
- Confirmed: IFR industrial robot installed-base data; Amazon disclosed robot fleet scale; Symbotic 10-K backlog/revenue concentration; Nabtesco precision reducer market-share estimate; A3/ANSI safety standard update.
- Management claims: NVIDIA Jetson Thor adoption/benefit claims; Agility Digit deployment framing; Google/NVIDIA robotics model capability claims.
- Inference: deployment integration, actuator durability and manipulation reliability are likely chokepoints if Physical AI deployments 10x.
- Speculation: consumer humanoids, universal humanoid factory labor, battery breakthrough pull-through, and world-model monetization before deployment proof.

## 6. Disconfirmation Checklist

See `physical_ai_disconfirmation_checklist.csv` for row-level tests. Cross-cutting disconfirmers:
- Repeat deployments do not arrive after pilots.
- Customers keep robots in fenced, narrow, low-throughput tasks with poor ROI.
- Service costs and downtime erase labor-productivity gains.
- Safety standards and insurance slow deployment more than expected.
- Commodity suppliers satisfy actuator/sensor demand without pricing power.
- Edge AI modules ship mostly as developer kits and do not convert into robot fleets.
- Simulation and world models fail to reduce exception rates in real sites.

## 7. Physical AI Chokepoint Ranking

1. **Safety-certified deployment, uptime, integration and maintenance capacity** (Testing / deployment / maintenance): Confirmed for industrial/warehouse automation; Inferred for humanoid scaling.; evidence E3-E5 for mature industrial/warehouse automation; E1-E2 for humanoids.; hype risk Low: this is a real deployment constraint, not a demo narrative..
2. **High-reliability motion stack: precision reducers, integrated joints, servo drives and thermal durability** (Actuators / motors / reducers): Confirmed for industrial robot reducers; Inferred for humanoid-specific ramp.; evidence E3-E4 industrial; E1-E2 humanoid.; hype risk Medium: the physical need is real, but humanoid volume assumptions are often speculative..
3. **Reliable perception and manipulation across SKU/object variance** (Perception / end effector / manipulation): Confirmed for constrained workflows; Inferred for generalized manipulation.; evidence E3-E4 for selected warehouse/industrial workflows; E1-E2 for general dexterity.; hype risk Medium: demos overstate generality if they omit exception rates and human fallback..
4. **On-robot inference under power, latency and heat constraints** (Edge compute / power / thermal co-design): Confirmed for product availability; Management claim / Inferred for scale adoption.; evidence E2-E3.; hype risk Medium: dev-kit availability is not the same as fleet revenue..
5. **Capex-heavy automation systems with real backlog but customer concentration and installation throughput risk** (Warehouse automation platform economics): Confirmed for selected warehouse automation; Inferred for broader Physical AI expansion.; evidence E4-E5 for leading warehouse automation; E2-E3 for newer humanoid add-ons.; hype risk Low to medium: real revenue exists, but concentration can create misleading backlog quality..
6. **Robot data scarcity and sim-to-real validation** (Simulation / synthetic data / world models): Management claim / Inferred.; evidence E1-E2 today unless connected to named customer production results.; hype risk High if not tied to real deployment improvement..
7. **Runtime and battery safety for mobile manipulators and humanoids** (Power / batteries): Inferred / Weak depending on claim.; evidence E0-E2 for humanoid battery miracle claims; E3 for certified AMR battery systems.; hype risk High when framed as solid-state battery miracle or humanoid adoption linchpin without deployment evidence..

Ranking buckets:
- High-confidence physical bottleneck: deployment/testing/maintenance; actuators/motion stack; perception/manipulation in constrained workflows.
- Medium-confidence bottleneck: edge compute/power/thermal co-design; warehouse automation installation throughput and system economics.
- Early but promising: simulation/synthetic data/world models when tied to real deployment improvement.
- Hype / no-go for now: consumer humanoids, demo-only humanoid claims, battery miracle narratives, partner-logo research without customer economics.

## 8. Serenity-Style Fit

Strong fit:
- Deployment/testing/maintenance: underfollowed, physical, certification-heavy, service-heavy, likely to contain smaller suppliers and integrators.
- Motion stack: reducer/servo/drive/control suppliers can be concentrated and qualification-bound.
- Perception/manipulation: attractive only when repeat deployment and exception-rate evidence exists.

Medium fit:
- Edge compute plus sensor bridge, power and thermal: the obvious compute layer is crowded, but second-order suppliers may be less followed.
- Warehouse automation systems: real revenue/backlog, but customer concentration and capex cycles must be controlled.

Weak fit / no-go for now:
- Pure model/demo claims without production data.
- Consumer humanoid general-purpose TAM narratives.
- Battery chemistry speculation without robotics deployment pull-through.

Before looking at companies, prove:
- repeat customer deployments;
- named production workflows;
- revenue/backlog linkage;
- field uptime and maintenance economics;
- safety certification path;
- supplier concentration or qualification lock-in;
- gross margin or cash-flow proof where available.

## 9. Later-Stage Public-Company Research Directions

This section is research direction only. It is not a current list of recommendations, not a current buy list, and not a valuation view.

| Label | Direction to research | Benchmark companies | Possible supplier category | No-go category |
|---|---|---|---|---|
| direction to research | Deployment/testing/integration bottleneck | ABB Robotics, Siemens, Rockwell Automation, Symbotic, Zebra Technologies | robot safety validation, system integration, field service, calibration, industrial QA | demo-only integrator logos without repeat deployment |
| direction to research | Precision motion stack | Nabtesco, Harmonic Drive Systems, Yaskawa, FANUC, Nidec | precision reducers, servo motors, drives, integrated joints, functional safety controllers | humanoid-volume extrapolation without OEM orders or capacity proof |
| direction to research | Machine vision and tactile manipulation | Cognex, Keyence, Zebra Technologies, Teradyne/Universal Robots, Schunk category peers | industrial vision, 3D sensing, force/tactile sensing, end-of-arm tooling | dexterity videos without exception-rate or customer economics |
| direction to research | Edge compute / sensor bridge / thermal | NVIDIA, Qualcomm, Analog Devices, Infineon, Advantech category peers | robot edge compute modules, deterministic sensor ingest, industrial power and thermal modules | dev-kit announcements treated as fleet revenue |
| direction to research | Warehouse automation real-economics lane | Symbotic, AutoStore, Zebra Technologies, Amazon Robotics as benchmark operator | AMR fleets, sorting/stowing cells, warehouse orchestration, installation services | single-customer backlog treated as universal adoption |
| direction to research | Simulation / synthetic data / world-model enablement | NVIDIA Isaac, Google DeepMind, Dassault Systemes, Siemens Digital Industries | robot simulation, digital twins, synthetic data, validation tooling | model demos without paid production deployment |
| no-go category | Consumer/general-purpose humanoid household adoption | Benchmark only: Boston Dynamics Atlas research, Figure/Agility/Apptronik private-company deployments | none until repeat revenue and safety evidence exist | consumer humanoid TAM slides, partner logos, conference videos |
| no-go category | Battery miracle thesis | Benchmark only: industrial BMS/power electronics suppliers | certified BMS, rugged packs, industrial charging | solid-state or energy-density claims without robot deployment pull-through |


## 10. Sources Used

- [International Federation of Robotics](https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years%20%20%20) - World Robotics 2025 press release: 2024 was the second-highest annual industrial robot installation count; operational robot stock reached 4.664 million units.
- [Amazon Robotics](https://www.aboutamazon.com/news/operations/amazon-robotics-robots-fulfillment-center) - Amazon says it has deployed more than 1 million robots across its operations network and describes production systems such as Sequoia, Hercules, Vulcan, Sparrow, Robin, Cardinal and Proteus.
- [BMW Group](https://www.bmwgroup.com/en/news/general/2024/humanoid-robots.html) - BMW describes Figure 02 as being tested at Plant Spartanburg in a real production environment; this is an early test operation, not proof of broad scale adoption.
- [Agility Robotics](https://www.agilityrobotics.com/content/digit-deployed-at-gxo-in-historic-humanoid-raas-agreement) - Agility says Digit deployment at GXO is part of a multi-year agreement and positioned in day-to-day logistics operations; evidence is company claim and early deployment, not public margin proof.
- [Symbotic FY2025 Form 10-K](https://ir.symbotic.com/static-files/a07466bc-96d1-484b-98fc-3efe41d3b8fb) - Symbotic reports Walmart as approximately 85% of FY2025 revenue and a significant majority of $22.5B backlog; validates warehouse automation demand but also customer concentration risk.
- [Nabtesco](https://www.nabtesco.com/en/products/robot/) - Nabtesco says its precision reduction gears are used in industrial robot joints and estimates about 60% global share for medium-to-large industrial robot precision reduction gears.
- [NVIDIA Jetson Thor newsroom](https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics) - NVIDIA says Jetson Thor is generally available, designed for physical AI/robotics, and targets real-time edge inference; claims about future adoption remain forward-looking.
- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) - NVIDIA describes Isaac Sim as a robotics simulation, testing and synthetic data generation framework for physically based virtual environments.
- [Google DeepMind Gemini Robotics](https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/) - Google DeepMind describes Gemini Robotics as vision-language-action models for robots to understand and act in the physical world; still primarily model capability evidence, not broad commercial revenue proof.
- [A3 / ANSI R15.06-2025](https://www.automate.org/industry-insights/ansi-a3-publish-revised-r15-06-industrial-robot-safety-standard) - A3 says the revised U.S. industrial robot safety standard was adapted from ISO 10218-1:2025 and ISO 10218-2:2025, reflecting safety/integration complexity.

## 11. Limitations

- Public-source synthesis only; no brokerage, private company data room, customer calls or channel checks.
- No financial model, no valuation, no target price, no entry point and no position sizing.
- Humanoid evidence is mostly E1-E2. Treat pilot claims as leads until repeat deployment, revenue and service economics are proven.
- Some benchmark companies are named only to define research directions and supply-chain categories; they are not recommendations.

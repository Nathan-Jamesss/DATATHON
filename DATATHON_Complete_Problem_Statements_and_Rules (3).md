# DATATHON — Official Track Brief, Dataset Guide & Competition Rules

**Format:** 7-hour, product-building Data Science / AI hackathon  
**Tracks:** 4 (each team chooses one)  
**Core expectation:** Build a working, data-powered product—not just a notebook, chart, or isolated ML model.

> **Dataset notice:** The downloadable starter pack contains synthetic educational data created for this event. It is not real patient, campus, city, or company data. It is designed to provide a consistent starting point across tracks. The data should not be used for real clinical, civic-safety, or business decisions.

## 1. What teams are expected to build

Each team receives one problem statement and its corresponding starter dataset. Teams should investigate the problem, identify a specific user, find useful patterns in the data, decide where Data Science/ML/optimization can add value, and build a working prototype.

A strong submission connects:

**Problem → User need → Data exploration → Model/logic → Recommendation/action → Product interface → Demonstration**

The ML model is a component of the product, not the whole product. A model with high accuracy but no useful workflow, explanation, or user-facing outcome is incomplete.

## 2. The four problem statements

### Track 1 — HEALTH: The Forgotten Patient

#### Problem statement
A patient’s experience in a hospital is a connected journey: arrival, triage, consultation, diagnostic tests, treatment, and discharge. When these stages are managed separately, delays and capacity issues can be difficult to spot early. Hospital teams need a clearer view of where patients are waiting, which services are under pressure, and where intervention may help.

**Challenge:** Build a hospital-flow product that helps staff understand patient journeys, identify likely bottlenecks, and make better-informed operational decisions.

**Primary users:** Hospital operations managers, department coordinators, and service administrators.

**Product outcomes could include:**
- A patient-flow dashboard with department-level queues and wait times.
- A forecast of demand or likely delays by department/time period.
- Alerts for unusual waiting patterns or potentially overloaded services.
- A diagnostic-test turnaround monitor.
- A “what should we investigate first?” queue ranked by impact and confidence.
- An explanation panel showing which data signals led to each alert.
- Optional IoT integration that processes simulated vital-sign/device streams and flags data requiring human review.

**Dataset foundation:** `01_health_forgotten_patient/`
- `patients.csv` — 2,000 patient profiles.
- `encounters.csv` — 8,000 visits with arrival, service, and discharge times.
- `departments.csv` — 12 departments with staffing/capacity attributes.
- `diagnostic_tests.csv` — 5,000 diagnostic-test records.
- `iot_vitals.csv` — 12,000 simulated device observations.

**How the data helps:** Teams can link visits to patients and departments, calculate wait and service patterns, compare departments, estimate test turnaround, study time-of-day demand, and build an operational view from several tables. The IoT table supports sensor-stream processing or anomaly detection. It is simulated and is **not** suitable for clinical diagnosis.

**Possible ML/data-science work:** Waiting-time regression, demand forecasting, clustering of visit patterns, anomaly detection, prioritization/ranking, or queue/resource optimization. Teams must use a time-aware split when evaluating predictions involving future time.

**Useful product question:** “What is likely to get delayed next, why, and what should the operations team examine?”

---

### Track 2 — EDUCATION: The Campus Has Space. Students Don’t.

#### Problem statement
Universities may have classrooms, laboratories, seminar rooms, and study spaces while students and clubs still struggle to find a suitable place at the right time. Some rooms may be underused, while others are in high demand. Fixed schedules and fragmented booking information make it hard to match actual demand to available capacity and facilities.

**Challenge:** Build a campus-space product that helps students find suitable rooms and helps administrators use existing campus space more effectively.

**Primary users:** Students, club coordinators, faculty, and campus facilities administrators.

**Product outcomes could include:**
- A room finder that matches time, capacity, accessibility, and facilities.
- A room-availability estimate using schedule and occupancy signals.
- A utilization dashboard showing where space is consistently underused.
- A recommendation engine for room allocation or event relocation.
- A demand forecast for busy days/time periods.
- An explanation for each match (“capacity fit, projector available, estimated occupancy low”).
- Optional IoT integration using occupancy/CO₂/light sensor data to estimate room use.

**Dataset foundation:** `02_education_campus_space/`
- `rooms.csv` — 120 room profiles.
- `class_schedule.csv` — 5,000 class-schedule records.
- `occupancy_iot.csv` — 25,000 simulated occupancy/sensor observations.
- `room_requests.csv` — 5,000 room requests.
- `events.csv` — 1,800 event records.

**How the data helps:** Room metadata defines capacity and facilities; schedules describe planned use; occupancy signals approximate actual use; requests represent demand; event records add non-classroom demand. Together, these allow teams to estimate utilization, identify schedule/occupancy mismatches, rank room matches, and suggest better allocations.

**Possible ML/data-science work:** Occupancy estimation, availability classification, demand forecasting, room recommendation/ranking, clustering of utilization patterns, or constrained room allocation. A valid solution should account for capacity, facilities, timing, and conflicting bookings—not merely predict occupancy.

**Useful product question:** “Given a room request, what is the best feasible room and what evidence supports that recommendation?”

---

### Track 3 — SMART CITY: Where Should We Fix First?

#### Problem statement
Cities receive reports about road damage, traffic, flooding, streetlights, drainage, and pedestrian safety. Budgets and field teams are limited, so not every issue can be handled at once. Authorities need a transparent way to combine incident history, public complaints, traffic conditions, and local context to decide which locations deserve attention first.

**Challenge:** Build a city-prioritization product that helps officials identify problem locations, understand the evidence behind their ranking, and compare possible interventions.

**Primary users:** Municipal operations teams, road/traffic departments, and civic-service coordinators.

**Product outcomes could include:**
- A map and ranked list of locations requiring attention.
- A complaint/incident trend monitor.
- A severity-and-frequency-based priority score.
- A sensor anomaly or traffic-congestion alert.
- A resolution-time dashboard for public complaints.
- A recommendation queue with reasons and confidence, not an unexplained “risk score.”
- Optional IoT integration using traffic and environmental sensor streams.

**Dataset foundation:** `03_smart_city_where_fix_first/`
- `locations.csv` — 1,000 simulated locations and context attributes.
- `incidents.csv` — 10,000 incident records.
- `traffic_iot.csv` — 18,000 simulated traffic observations.
- `public_complaints.csv` — 8,000 complaint records.
- `environment_iot.csv` — 12,000 simulated environmental sensor observations.

**How the data helps:** The common `location_id` allows incidents, complaints, road conditions, traffic, and sensor readings to be brought together. Teams can aggregate repeated issues, estimate patterns over time, compare zones, and create a transparent intervention-priority list.

**Possible ML/data-science work:** Incident-volume forecasting, complaint-category classification, resolution-time estimation, anomaly detection, location ranking, or resource-allocation optimization. Teams should explain limitations and avoid claiming the synthetic coordinates represent real locations.

**Useful product question:** “Which locations should be reviewed first, based on what evidence, and what information is still missing?”

---

### Track 4 — BUSINESS: The Money Leak

#### Problem statement
A business can record thousands of transactions and still struggle to understand why revenue or margin is underperforming. Cancellations, returns, discounts, stockouts, customer changes, and marketing spend can tell different parts of the story. These signals are often spread across separate systems, making it difficult to turn raw records into a clear action.

**Challenge:** Build a business decision-support product that helps a manager identify potential revenue or operational problems, investigate their likely drivers, and decide what to do next.

**Primary users:** Business owners, retail managers, product/category managers, and operations teams.

**Product outcomes could include:**
- A revenue, cancellation, and return investigation dashboard.
- A customer/product/region breakdown of performance.
- A stockout and inventory-risk monitor.
- A campaign-efficiency view connecting spend, clicks, and conversions.
- A forecast or alert for unusual performance changes.
- A “why this is flagged” panel with supporting metrics.
- Optional IoT integration using store footfall, queue, and device-status signals.

**Dataset foundation:** `04_business_money_leak/`
- `customers.csv` — 3,000 customer profiles.
- `products.csv` — 250 product records.
- `transactions.csv` — 18,000 transaction records.
- `inventory.csv` — 5,000 inventory observations.
- `campaigns.csv` — 1,200 campaign records.
- `retail_iot.csv` — 10,000 simulated retail sensor observations.

**How the data helps:** Transaction records can be joined with customer and product information to study sales and status patterns. Inventory records add stock availability; campaigns add marketing context; retail IoT records add store activity and checkout queue signals. Teams can define useful business metrics and build a product around investigation and action rather than a generic sales chart.

**Possible ML/data-science work:** Cancellation/return classification, demand forecasting, customer segmentation, anomaly detection, stockout-risk estimation, campaign conversion analysis, or inventory optimization. Teams must document assumptions about costs, prices, returns, and profit calculations.

**Useful product question:** “What appears to be going wrong, what evidence supports that finding, and what action should the manager consider?”

---

## 3. Dataset inventory and comparable scope

The four starter datasets are designed to have similar breadth: multiple related tables, time-based records, numerical and categorical features, and an IoT/sensor table. Their row counts are not identical because the natural entities differ, but each track supports joining, cleaning, feature engineering, modelling, and a product interface.

| Track | CSV files | Total rows across files | IoT/sensor table |
|---|---:|---:|---:|
| Health | 5 | 27,012 | 12,000 observations |
| Education | 5 | 36,920 | 25,000 observations |
| Smart City | 5 | 49,000 | 30,000 observations across traffic/environment |
| Business | 6 | 37,450 | 10,000 observations |

**Fairness note:** Row count alone is not a measure of difficulty. Judges should assess the reasoning, quality of the product, data usage, validation, and usefulness—not who processed the most rows. All four datasets are synthetic, and no track comes with a guaranteed “correct model” or required target column.

### Recommended first steps for every team
1. Read the track README and inspect all tables.
2. Check row counts, missing values, duplicate keys, ranges, and timestamp coverage.
3. Draw a small data-relationship diagram and decide which tables need to be joined.
4. Define the product user and one high-value workflow.
5. Choose a measurable data-science objective that supports that workflow.
6. Create a simple baseline before trying a more complex model.
7. Validate the model/logic, then connect it to the product interface.
8. Show a complete example from input → analysis/model → output → user action.

## 4. IoT and original ML model expectations

Original modelling and meaningful IoT integration are encouraged. They should receive strong credit **when they improve the product**, not merely because a model or sensor is present.

### What counts as an original trained model?
- The team defines a prediction, classification, ranking, forecasting, or anomaly-detection task.
- The team trains or meaningfully fine-tunes a model using the provided dataset or permitted additional data.
- The team documents features, target/label, split strategy, baseline, evaluation metric, and limitations.
- The trained model is connected to the working product and its output changes a real workflow, alert, recommendation, or decision.

Pretrained APIs or LLM calls may be used as supporting components, but do not count by themselves as a team-trained ML model.

### What counts as meaningful IoT work?
- Ingesting sensor data (live, replayed, or simulated) in a clearly explained pipeline.
- Handling timestamps, missing/noisy readings, device status, or streaming updates.
- Using sensor signals in a model or product decision.
- Demonstrating the sensor-to-model-to-interface path.

Physical hardware is optional unless the organizers announce otherwise. A sensor-data replay or simulator is acceptable if clearly labelled. A decorative sensor graphic with no data flow does not qualify.

### Fair scoring principle
Do **not** award extra marks solely for having IoT hardware or a complicated algorithm. Award marks for original modelling, sound evaluation, integration, reliability, and demonstrated user value. Teams in every track have an IoT dataset so this opportunity is not exclusive to one track.

## 5. Rules

1. **Choose one track.** Build against the corresponding problem statement and starter dataset.
2. **The provided dataset is foundational.** Teams may add relevant public data, APIs, or self-collected data if permitted, but must still use the supplied dataset meaningfully.
3. **Disclose additional data.** Include source, licence/permission, collection method, and what it contributes.
4. **No replacing the core dataset.** A product that ignores the provided data and relies entirely on an external API will lose data-use marks.
5. **Build a product, not only a model.** A notebook, static chart, or model file alone is not a complete submission.
6. **Model claims must be supported.** Report the evaluation method and appropriate metrics. Do not claim “high accuracy” without showing evidence.
7. **Prevent leakage.** Use time-based or group-based splits where appropriate; avoid using future information to predict the past.
8. **Explain the result.** A user should understand why a prediction, alert, or recommendation appeared.
9. **Synthetic data limitations must be acknowledged.** Teams cannot claim the generated data proves real-world performance.
10. **Responsible use.** No real personal/medical records, unauthorized access, unsafe live deployment, or misleading public-safety claims.
11. **Use permitted tools.** Teams should disclose significant third-party APIs, pretrained models, and external services.
12. **Demonstrate the workflow.** Judges should be able to see a real input and a useful product output.
13. **One overall competition.** All tracks use the same judging rubric and compete for the same prizes.
14. **Submission freeze.** Teams must submit their source/demo and presentation by the deadline announced by organizers.
15. **Team integrity.** Teams must identify borrowed code, datasets, models, and templates. Plagiarism or fabricated evaluation results may lead to disqualification.

## 6. Judging rubric — 100 marks

| Criterion | Marks | What judges look for |
|---|---:|---|
| Problem understanding and user need | 10 | Clear user, pain point, and scope |
| Provided dataset usage | 15 | Meaningful joins, analysis, features, and data-driven decisions |
| Data Science / ML quality | 15 | Appropriate method, baseline, evaluation, and reasoning |
| Original trained model | 10 | Team-trained/fine-tuned model integrated into the solution |
| IoT / sensor integration | 10 | Useful sensor pipeline and impact on product decisions |
| Working product and workflow | 20 | Functional end-to-end prototype, usability, and reliability |
| USP and innovation | 10 | Differentiation and quality of solution |
| Impact, feasibility, and responsible use | 5 | Plausible benefit, limitations, and responsible claims |
| Demo and presentation | 5 | Clear demonstration and communication |
| **Total** | **100** | |

**Weighting clarification:** Original ML (10) and IoT (10) are explicit scoring areas. Judges should score what is actually demonstrated; teams should not receive full marks merely for stating that they trained a model or used IoT. If an IoT/ML approach is genuinely unsuitable for a specific product decision, judges may consider the quality of the justified alternative under the relevant technical/product categories, while applying the published rubric consistently.

## 7. Minimum complete-product checklist

A submission should include:
- [ ] Named product and target user.
- [ ] Clear problem and value proposition / USP.
- [ ] Data exploration and documented data cleaning.
- [ ] A meaningful use of the provided dataset.
- [ ] A baseline and evaluated ML/statistical/optimization component where appropriate.
- [ ] IoT/sensor integration or a clear, technically justified alternative.
- [ ] Usable interface: web app, dashboard, mobile prototype, API, or equivalent.
- [ ] At least one end-to-end workflow demonstrated.
- [ ] Recommendations, alerts, or outputs explained in user terms.
- [ ] Limitations and next steps.
- [ ] Short presentation and live demo.

## 8. Suggested seven-hour working plan

| Time | Focus | Expected checkpoint |
|---|---|---|
| 10:00–10:20 | Briefing and rules | Understand the problem and constraints |
| 10:20–11:00 | Data audit and research | Identify user, data relationships, and key question |
| 11:00–12:30 | Baseline and product skeleton | First useful analysis/model and working interface |
| 12:30–1:00 | Progress checkpoint | Confirm a realistic MVP scope |
| 1:00–1:30 | Lunch | — |
| 1:30–3:30 | Build and integrate | Model/logic connected to product |
| 3:30–4:30 | Test and improve | Validate results and complete workflow |
| 4:30–5:00 | Finalize submission | Demo and slides ready |
| 5:00–6:00 | Presentations and evaluation | Judges assess the prototype |
| 6:00–7:00 | Prize distribution and closing | Results and closing |

## 9. Downloadable dataset pack

The accompanying ZIP contains all four tracks, the CSV files, and a README for each track. Use the folder for the chosen track. These starter data are synthetic and intended to be the common foundation for the competition.

**Organizer preparation before release:** Check the generated CSVs, publish the same pack to every team, and announce whether teams may use internet access, external datasets, hosted APIs, and physical IoT devices. Do not change dataset difficulty or provide extra private labels to selected teams after the event begins.

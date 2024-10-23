//Project title
# Project ArXiv Citation Network

//students names
## Students
- [Name1](Leo Ho)
- [Name2](Minh Tran)

//School name
## School
- [School Name](Grand Valley State University)

//Project intro
## 1. Introduction
This project is to analyze the citation network of ArXiv papers. We will use the data from two specific file "data\oai-arxiv-metadata-hash-abstracts-2019-03-01.json" and "data\internal-references-pdftotext.json" to get the citation information of the papers using pythong code to clean data and create neo4j network. We will then use the data to analyze the citation network of ArXiv papers.

//Data description
## 2. Data Description
- I collected this data using the ArXiv API. The data is in JSON format and contains the metadata of the papers. The data includes the title, authors, abstract, and references of the papers. The data is stored in two files: "data\oai-arxiv-metadata-hash-abstracts-2019-03-01.json" and "data\internal-references-pdftotext.json". After having the needed data, I used Python to clean the data and create a Neo4j network.

- By watching the neo4j graph database using the command `MATCH (n) RETURN n`, I can see the citation network of the ArXiv papers. The nodes represent the papers, and category and the edges represent the citations between the papers and category between them. There are two different kinds of nodes in the graph: `Paper` and `Categorie`. The papers are connected to the categories by the `CATEGORIZED` relationship. The papers are connected to each other by the `CITES` relationship.

- The `Paper` nodes have 9 attributes including `elementId` - the element Id of the paper, `id` - the identifier of the paper in the database, `abstract_md5` - the MD5 hash of the abstract of the paper, `authors` - the list of authors of the paper, ,`doi` - the Digital Object Identifier of the paper, `idAxv` - the identifier of the paper in the ArXiv database, `report_no` - the report number of the paper, `submitter` - the submitter of the paper, `title` - the title of the paper. The `Category` nodes have 3 attributes including `elementId` - the element Id of the category, `id` - the indentifier of the category in neo4j graph, `category` - the name of the category. 

- The `CATEGORIZED` relationship has 2 attributes including `elementId` - the element Id of the relationship, `id` - the identifier of the relationship in the database. The `CITES` relationship has 2 attributes including `elementId` - the element Id of the relationship, `id` - the identifier of the relationship in the database.

There are 313 nodes and 667 relationships by reviewing the neo4j graph database.
//picture of the graph
![Graph Screenshot](pictures/Screenshot%202024-10-22%20130356.png)

//Analysis
## 3. Analysis
//network metrics
### 3.1 Network Metrics
Composites:
- The average number of cited for each paper is : 0.783 
- This shows that each paper in the dataset is cited approximately 0.783 times by other papers. This suggests that not all papers are cited frequently, and some papers are not be cited at all.
![Graph Screenshot](pictures/Screenshot%202024-10-22%20135755.png)
- The number of paper for each category:
![Graph Screenshot](pictures/Screenshot%202024-10-22%140851.png)
╒════════════════════╤═══════════════╕
│category_name       │number_of_paper│
╞════════════════════╪═══════════════╡
│"hep-ph"            │95             │
├────────────────────┼───────────────┤
│"hep-th"            │80             │
├────────────────────┼───────────────┤
│"astro-ph"          │73             │
├────────────────────┼───────────────┤
│"gr-qc"             │28             │
├────────────────────┼───────────────┤
│"hep-ex"            │22             │
├────────────────────┼───────────────┤
│"quant-ph"          │17             │
├────────────────────┼───────────────┤
│"math.MP"           │13             │
├────────────────────┼───────────────┤
│"math-ph"           │13             │
├────────────────────┼───────────────┤
│"cond-mat.mes-hall" │8              │
├────────────────────┼───────────────┤
│"math.AG"           │8              │
├────────────────────┼───────────────┤
│"cond-mat.other"    │7              │
├────────────────────┼───────────────┤
│"nucl-th"           │7              │
├────────────────────┼───────────────┤
│"math.QA"           │7              │
├────────────────────┼───────────────┤
│"cond-mat.stat-mech"│6              │
├────────────────────┼───────────────┤
│"cond-mat.mtrl-sci" │6              │
├────────────────────┼───────────────┤
│"cond-mat.dis-nn"   │5              │
├────────────────────┼───────────────┤
│"math.CV"           │5              │
├────────────────────┼───────────────┤
│"cond-mat.str-el"   │5              │
├────────────────────┼───────────────┤
│"math.GR"           │4              │
├────────────────────┼───────────────┤
│"math.RT"           │4              │
├────────────────────┼───────────────┤
│"math.DG"           │4              │
├────────────────────┼───────────────┤
│"nucl-ex"           │4              │
├────────────────────┼───────────────┤
│"hep-lat"           │3              │
├────────────────────┼───────────────┤
│"math.SG"           │3              │
├────────────────────┼───────────────┤
│"math.RA"           │3              │
├────────────────────┼───────────────┤
│"math.DS"           │2              │
├────────────────────┼───────────────┤
│"math.CO"           │2              │
├────────────────────┼───────────────┤
│"cond-mat.supr-con" │2              │
├────────────────────┼───────────────┤
│"math.NT"           │2              │
├────────────────────┼───────────────┤
│"physics.soc-ph"    │2              │
├────────────────────┼───────────────┤
│"nlin.SI"           │2              │
├────────────────────┼───────────────┤
│"math.GT"           │2              │
├────────────────────┼───────────────┤
│"physics.data-an"   │2              │
├────────────────────┼───────────────┤
│"q-fin.ST"          │2              │
├────────────────────┼───────────────┤
│"math.GN"           │1              │
├────────────────────┼───────────────┤
│"cs.DM"             │1              │
└────────────────────┴───────────────┘
-The number of being cited for each paper:
![Graph Screenshot](pictures/Screenshot%202024-10-22%142658.png)
╒══════════════════════════════════════════════════════════════════════╤═══════════════╕
│tittle                                                                │number_of_cited│
╞══════════════════════════════════════════════════════════════════════╪═══════════════╡
│"Stringy Instantons at Orbifold Singularities"                        │3              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Analytic solutions for marginal deformations in open superstring fiel│3              │
│d  theory"                                                            │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Marginal Solutions for the Superstring"                              │3              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Charges from Attractors"                                             │3              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Direct extraction of one-loop integral coefficients"                 │3              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Numerical Evaluation of Six-Photon Amplitudes"                       │3              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A data-analysis driven comparison of analytic and numerical coalescin│3              │
│g  binary waveforms: nonspinning case"                                │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The S-parameter in Holographic Technicolor Models"                   │3              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A Search for Electron Neutrino Appearance at the Delta m             |2              |
|<sup>2</sup> ~ 1 eV<sup>2</sup> Scale"                                │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Phenomenology with Massive Neutrinos"                                │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Implication of the D^0 Width Difference On CP-Violation in D^0-\bar D│2              │
│^0  Mixing"                                                           │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Measurement of D0-D0bar mixing in D0->Ks pi+ pi- decays"             │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Quantum Hall Effect in a Graphene p-n Junction"                      │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Measurement of B(D_S^+ --> ell^+ nu) and the Decay Constant f_D_{S^+}│2              │
│"                                                                     │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Dynamical Casimir effect for gravitons in bouncing braneworlds"      │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Strong Phase and $D^0-D^0bar$ mixing at BES-III"                     │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"D-\bar D mixing and rare D decays in the Littlest Higgs model with  n│2              │
│on-unitarity matrix"                                                  │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The dynamical Casimir effect in braneworlds"                         │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"An exact sequence for contact- and symplectic homology"              │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Fractal dimension of domain walls in two-dimensional Ising spin glass│2              │
│es"                                                                   │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Averages of b-hadron properties at the end of 2006"                  │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Pseudo-supersymmetry and a Tale of Alternate Realities"              │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Two Results on Homogeneous Hessian Nilpotent Polynomials"            │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Electroweak Higgs as a pseudo-Goldstone boson of broken scale invaria│2              │
│nce"                                                                  │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Route to Lambda in conformally coupled phantom cosmology"            │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Measuring the dark side (with weak lensing)"                         │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Symplectic homology, autonomous Hamiltonians, and Morse-Bott moduli  │2              │
│spaces"                                                               │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The S-Matrix of AdS/CFT and Yangian Symmetry"                        │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Determination of the Helicity of $W'$ Boson Couplings at the LHC"│2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Reconciling the X(3872) with the near-threshold enhancement in the  D│2              │
│^0\bar{D}^{*0} final state"                                           │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Improved Measurement of the Positive Muon Lifetime and Determination │2              │
│of  the Fermi Constant"                                               │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Measurement of the Rate of Muon Capture in Hydrogen Gas and  Determin│2              │
│ation of the Proton's Pseudoscalar Coupling $g_P$"                    │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Resolving Cosmic Gamma Ray Anomalies with Dark Matter Decaying Now"  │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Collider signals in unparticle physics"                              │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Study of B+ to p Lambdabar gamma, p Lambdabar pi0 and B0 to p Lambdab│2              │
│ar  pi-"                                                              │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A method for the direct determination of the surface gravities of  tr│2              │
│ansiting extrasolar planets"                                          │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Flavour-Dependent Type II Leptogenesis"                              │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Scaling cosmologies, geodesic motion and pseudo-susy"                │2              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Swift/XRT observes the fifth outburst of the periodic Supergiant Fast│1              │
│  X-ray Transient IGR J11215-5952"                                    │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Quantum Hacking: Experimental demonstration of time-shift attack agai│1              │
│nst  practical quantum key distribution systems"                      │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Cosmological constraints combining H(z), CMB shift and SNIa  observat│1              │
│ional data"                                                           │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"ATLAS Discovery Potential for the Charged Higgs Boson in H+ to tau nu│1              │
│  Decays"                                                             │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Jumping Through Loops: On Soft Terms from Large Volume Compactificati│1              │
│ons"                                                                  │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Type I singularities and the Phantom Menace"                         │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Bubbling Surface Operators And S-Duality"                            │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Bubbling AdS and droplet descriptions of BPS geometries in IIB  super│1              │
│gravity"                                                              │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Limits on WIMP-nucleon interactions with CsI(Tl) crystal detectors"  │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Sparticle Spectra and LHC Signatures for Large Volume String  Compact│1              │
│ifications"                                                           │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Lee-Wick Standard Model"                                         │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Testing the Standard Model by precision measurement of the weak charg│1              │
│es  of quarks"                                                        │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A Measure of de Sitter Entropy and Eternal Inflation"                │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Another Odd Thing About Unparticle Physics"                          │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Exact Mapping of the 2+1 Dirac Oscillator onto the Jaynes-Cummings  M│1              │
│odel: Ion-Trap Experimental Proposal"                                 │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Relativistic Hydrodynamics at RHIC and LHC"                          │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A calculation of the shear viscosity in SU(3) gluodynamics"          │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Many-Body Physics with Ultracold Gases"                              │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Mathematical Universe"                                           │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Anomalous dimensions at twist-3 in the sl(2) sector of N=4 SYM"      │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Braneworld Cosmology"                                                │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Phantom field dynamics in loop quantum cosmology"                    │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Density dependent hadronic models and the relation between neutron st│1              │
│ars  and neutron skin thickness"                                      │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Transport measurements across a tunable potential barrier in graphene│1              │
│"                                                                     │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Marginal deformations in string field theory"                        │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Gauge Mediation in String Theory"                                    │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Casimir Force in Randall Sundrum Models"                         │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Light projectile scattering off the Color Glass Condensate"          │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Boundaries and the Casimir effect in non-commutative space-time"     │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Casimir effect in a 6D warped flux compactification model"           │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Reconstruction Algebras of Type A"                                   │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Dressing and Wrapping"                                               │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Orbifolds of Permutation-Type as Physical String Systems at  Mult│1              │
│iples of $c=26$ III. The Spectra of $\hat{c}=52$ Strings"             │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Special McKay correspondence as an equivalence of derived categor│1              │
│ies"                                                                  │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Mapping the Cosmological Confidence Ball Surface"                    │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Probing dark energy with steerable wavelets through correlation of WM│1              │
│AP  and NVSS local morphological measures"                            │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Halo-model signatures from 380,000 SDSS Luminous Red Galaxies with  p│1              │
│hotometric redshifts"                                                 │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Search for gravitational waves from binary inspirals in S3 and S4 LIG│1              │
│O  data"                                                              │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Epps effect revisited"                                           │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Right-Handed Quark Mixings in Minimal Left-Right Symmetric Model with│1              │
│  General CP Violation"                                               │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"An algorithm for the classification of smooth Fano polytopes"        │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"On-Shell Methods in Perturbative QCD"                                │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Placeholder Substructures III: A Bit-String-Driven ''Recipe Theory'' │1              │
│for  Infinite-Dimensional Zero-Divisor Spaces"                        │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Placeholder Substructures II: Meta-Fractals, Made of Box-Kites, Fill │1              │
│ Infinite-Dimensional Skies"                                          │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"GRB 061121: Broadband spectral evolution through the prompt and  afte│1              │
│rglow phases of a bright burst"                                       │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"D-brane Instantons on the T^6/Z_3 orientifold"                       │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Multiple Unfoldings of Orbifold Singularities: Engineering Geometric │1              │
│ Analogies to Unification"                                            │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Complex data processing: fast wavelet analysis on the sphere"        │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Signal for space-time noncommutativity: the Z -> gamma gamma decay in│1              │
│  the renormalizable gauge sector of the theta-expanded NCSM"         │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Lower order terms in the 1-level density for families of holomorphic │1              │
│ cuspidal newforms"                                                   │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"On the Origin of the Dichotomy of Early-Type Galaxies: The Role of Dr│1              │
│y  Mergers and AGN Feedback"                                          │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Isophotal Structure of Early-Type Galaxies in the SDSS: Dependenc│1              │
│e  on AGN Activity and Environment"                                   │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Heisenberg antiferromagnet with anisotropic exchange on the Kagome  l│1              │
│attice: Description of the magnetic properties of volborthite"        │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Real analytic solutions for marginal deformations in open superstring│1              │
│  field theory"                                                       │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Curvature flows in semi-Riemannian manifolds"                        │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"String inspired explanation for the super-acceleration of our univers│1              │
│e"                                                                    │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Strong decays of charmed baryons"                                    │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Search for Heavy Neutral MSSM Higgs Bosons with CMS: Reach and  Higgs│1              │
│-Mass Precision"                                                      │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Droplets in the two-dimensional +-J spin glass: evidence for (non-)  │1              │
│universality"                                                         │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Entanglement entropy at infinite randomness fixed points in higher  d│1              │
│imensions"                                                            │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Goldberger-Miyazawa-Oehme sum rule revisited"                    │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"One-loop phi-MHV amplitudes using the unitarity bootstrap"           │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"High Energy Afterglow from Gamma-ray Bursts"                         │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Dynamics of a quantum phase transition in a ferromagnetic Bose-Einste│1              │
│in  condensate"                                                       │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Spin Evolution of Accreting Neutron Stars: Nonlinear Development of t│1              │
│he  R-mode Instability"                                               │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Monoid generalizations of the Richard Thompson groups"               │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Constraints on Regge models from perturbation theory"                │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Contraints on radiative dark-matter decay from the cosmic microwave  │1              │
│background"                                                           │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Diffuse cosmic gamma-rays at 1-20 MeV: A trace of the dark matter?"  │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Some Properties of and Open Problems on Hessian Nilpotent Polynomials│1              │
│"                                                                     │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Measurement Calculus"                                            │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Green's function of a finite chain and the discrete Fourier transform│1              │
│"                                                                     │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Bouncing Universe with Quintom Matter"                               │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Numerical solution of shock and ramp compression for general material│1              │
│  properties"                                                         │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Instanton Induced Neutrino Majorana Masses in CFT Orientifolds with  │1              │
│MSSM-like spectra"                                                    │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A Way to Dynamically Overcome the Cosmological Constant Problem"     │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Domain wall entropy of the bimodal two-dimensional Ising spin glass" │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Finite bias visibility of the electronic Mach-Zehnder interferometer"│1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Kirillov-Reshetikhin conjecture : the general case"                  │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Second-order perturbations of cosmological fluids: Relativistic effec│1              │
│ts  of pressure, multi-component, curvature, and rotation"            │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A compact star rotating at 1122 Hz and the r-mode instability"       │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Epitaxial graphene"                                                  │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Direct photons and dileptons via color dipoles"                      │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A Survey of Huebschmann and Stasheff's Paper: Formal Solution of the │1              │
│ Master Equation via HPT and Deformation Theory"                      │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Counting BPS operators in N=4 SYM"                                   │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Dynamics of Quintessence, The Quintessence of Dynamics"          │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Polymer Quantum Mechanics and its Continuum Limit"                   │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Lattice refining loop quantum cosmology, anisotropic models and  stab│1              │
│ility"                                                                │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Two-loop QED corrections to Bhabha scattering"                       │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The angular correlations of galaxies in the COSMOS field"            │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Vortex proliferation in the Berezinskii-Kosterlitz-Thouless regime on│1              │
│ a  two-dimensional lattice of Bose-Einstein condensates"             │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"An Inverse $f(R)$ Gravitation for Cosmic Speed up, and Dark Energy  E│1              │
│quivalent"                                                            │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Generalization of Einstein-Lovelock theory to higher order dilaton  g│1              │
│ravity"                                                               │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Extra force in $f(R)$ modified theories of gravity"                  │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Supersymmetry breaking metastable vacua in runaway quiver gauge theor│1              │
│ies"                                                                  │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Redefining the Missing Satellites Problem"                           │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Equation of State in Relativistic Magnetohydrodynamics: variable vers│1              │
│us  constant adiabatic index"                                         │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Higher Nilpotent Analogues of A-infinity Structure"                  │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Dynamic rays of bounded-type entire functions"                       │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Measurement of the Decay Constant $f_D{_S^+}$ using $D_S^+ --> ell^+ │1              │
│nu"                                                                   │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Observation of the Decay \bar{B0}-> Ds+ Lambda \bar{p}"              │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Representations admitting two pairs of supplementary invariant spaces│1              │
│"                                                                     │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Constraints on the Very Early Universe from Thermal WIMP Dark Matter"│1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Possible solution to the $^7$Li problem by the long lived stau"      │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"One-loop MHV Rules and Pure Yang-Mills"                              │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Combinatorial structure of Kirillov-Reshetikhin crystals of type D_n(│1              │
│1),  B_n(1), A_{2n-1}(2)"                                             │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A sequence of blowing-ups connecting moduli of sheaves and the Donald│1              │
│son  polynomial under change of polarization"                         │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A-infinity structure on simplicial complexes"                        │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Blazar Spectral Sequence and GLAST"                              │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Extended solar emission - an analysis of the EGRET data"             │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Spectral Index Distribution of EGRET Blazars: Prospects for GLAST│1              │
│"                                                                     │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Ultra-High Energy Cosmic Rays and the GeV-TeV Diffuse Gamma-Ray Flux"│1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"The Mass and Radius of the Unseen M-Dwarf Companion in the Single-Lin│1              │
│ed  Eclipsing Binary HAT-TR-205-013"                                  │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Renormalization group flows and quantum phase transitions: fidelity  │1              │
│versus entanglement"                                                  │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Fidelity approach to quantum phase transitions: finite size scaling f│1              │
│or  quantum Ising model in a transverse field"                        │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Projective Hilbert space structures at exceptional points"           │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Canonical Deformed Groups of Diffeomorphisms and Finite Parallel  Tra│1              │
│nsports in Riemannian Spaces"                                         │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Entanglement increase from local interactions with  not-completely-po│1              │
│sitive maps"                                                          │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Group-theoretic Description of Riemannian Spaces"                    │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"A practical Seedless Infrared-Safe Cone jet algorithm"               │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Controlled collisions of a single atom and ion guided by movable  tra│1              │
│pping potentials"                                                     │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Strong photon non-linearities and photonic Mott insulators"          │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Developing the Galactic diffuse emission model for the GLAST Large Ar│1              │
│ea  Telescope"                                                        │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Semiclassical Quantization of the Giant Magnon"                      │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Vector mesons from AdS/TC to the LHC"                                │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Generalized MICZ-Kepler Problems and Unitary Highest Weight Modules -│1              │
│-  II"                                                                │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Fermionic formulas for (1,p) logarithmic model characters in \Phi_{2,│1              │
│1}  quasiparticle realisation"                                        │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"I. The mass gap and solution of the quark confinement problem in QCD"│1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Long Distance Signaling Using Axion-like Particles"                  │1              │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Experimental Challenges Involved in Searches for Axion-Like Particles│1              │
│  and Nonlinear Quantum Electrodynamic Effects by Sensitive Optical Te│               │
│chniques"                                                             │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Impact of spin-zero particle-photon interactions on light polarizatio│1              │
│n  in external magnetic fields"                                       │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Signatures of axion-like particles in the spectra of TeV gamma-ray  s│1              │
│ources"                                                               │               │
├──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Non-Abelian Chern-Simons Vortices"                                   │1              │
└──────────────────────────────────────────────────────────────────────┴───────────────┘
- The author with more than 1 paper:
![Graph Screenshot](pictures/Screenshot%202024-10-22%143433.png)
╒═════════════════════════════════════════════╤════════════════╕
│author_name                                  │number_of_papers│
╞═════════════════════════════════════════════╪════════════════╡
│"Robert P. C. de Marrais"                    │2               │
├─────────────────────────────────────────────┼────────────────┤
│"Thomas G. Rizzo"                            │2               │
├─────────────────────────────────────────────┼────────────────┤
│"Claus Gerhardt"                             │2               │
├─────────────────────────────────────────────┼────────────────┤
│"Jacob L. Bourjaily"                         │2               │
├─────────────────────────────────────────────┼────────────────┤
│"Steven J. Miller"                           │2               │
├─────────────────────────────────────────────┼────────────────┤
│"Yuji Okawa (DESY)"                          │2               │
├─────────────────────────────────────────────┼────────────────┤
│"Fr\'ed\'eric Bourgeois and Alexandru Oancea"│2               │
├─────────────────────────────────────────────┼────────────────┤
│"Wenhua Zhao"                                │2               │
├─────────────────────────────────────────────┼────────────────┤
│"V. Gogokhia"                                │2               │
├─────────────────────────────────────────────┼────────────────┤
│"J. Hwang and H. Noh"                        │2               │
├─────────────────────────────────────────────┼────────────────┤
│"V.Dolotin, A.Morozov and Sh.Shakirov"       │2               │
├─────────────────────────────────────────────┼────────────────┤
│"Kimiko Yamada"                              │2               │
├─────────────────────────────────────────────┼────────────────┤
│"Guowu Meng"                                 │2               │
├─────────────────────────────────────────────┼────────────────┤
│"Serhiy E. Samokhvalov"                      │2               │
└─────────────────────────────────────────────┴────────────────┘
Maximums:
- The table shows that the most popular category is "hep-ph" with 95 papers, followed by "hep-th" with 80 papers. The least popular categories are "math.GN" and "cs.DM" with only 1 paper each.
- The most important paper is ""Stringy Instantons at Orbifold Singularities" with being cited 3 times.
- The max papers by an author is 2, and there are 13 authors with 2 papers.
Density:
- The density of the network is 217(number of `CITES` links) / 38226(total number of `PAPER` nodes pairs) = 0.005 which is very low. This means that the network is very sparse. That is make sense in citatioin networks because not all papers are cited by all other papers and vice versa.
//Node pair metrics
### 3.2 Node pair metrics
- The most cocitation:
![Graph Screenshot](pictures/Screenshot%202024-10-22%192236.png)
- We picked the top 4 cocitation pairs to show the most cocitation pairs since the table is too long to show all of them.
╒══════════════════════════════════════════════════════════════════════╤══════════════════════════════════════════════════════════════════════╤═══════════════╕
│Paper1                                                                │Paper2                                                                │CoCitationCount│
╞══════════════════════════════════════════════════════════════════════╪══════════════════════════════════════════════════════════════════════╪═══════════════╡
│"Strong Phase and $D^0-D^0bar$ mixing at BES-III"                     │"D-\bar D mixing and rare D decays in the Littlest Higgs model with  n│2              │
│                                                                      │on-unitarity matrix"                                                  │               │
├──────────────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Marginal Solutions for the Superstring"                              │"Analytic solutions for marginal deformations in open superstring fiel│2              │
│                                                                      │d  theory"                                                            │               │
├──────────────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Numerical Evaluation of Six-Photon Amplitudes"                       │"Direct extraction of one-loop integral coefficients"                 │2              │
├──────────────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────────────┼───────────────┤
│"Improved Measurement of the Positive Muon Lifetime and Determination │"Measurement of the Rate of Muon Capture in Hydrogen Gas and  Determin│2              │
│of  the Fermi Constant"                                               │ation of the Proton's Pseudoscalar Coupling $g_P$"                    │               │
└──────────────────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────────────┴───────────────┘
- The table is make sense since the most cocitation pairs are the pairs that are related to each other. For example, the first pair is about the mixing of D mesons and the second pair is about the marginal solutions for the superstring.
- The most bibliographic coupling:
![Graph Screenshot](pictures/Screenshot%202024-10-22%193439.png)
╒══════════════════════════════════════════════════════════╤══════════════════════════════════════════════════════════╤══════════════════════════╕
│Paper1                                                    │Paper2                                                    │BibliographicCouplingCount│
╞══════════════════════════════════════════════════════════╪══════════════════════════════════════════════════════════╪══════════════════════════╡
│"Implication of the D^0 Width Difference On CP-Violation i│"D0-anti-D0 Mixing and CP Violation in D0 vs anti-D0 to K*│2                         │
│n D^0-\bar D^0  Mixing"                                   │(+-) K(-+)  Decays"                                       │                          │
├──────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────┼──────────────────────────┤
│"Marginal deformations in string field theory"            │"Real analytic solutions for marginal deformations in open│2                         │
│                                                          │ superstring  field theory"                               │                          │
├──────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────┼──────────────────────────┤
│"On-Shell Methods in Perturbative QCD"                    │"One-loop phi-MHV amplitudes using the unitarity bootstrap│2                         │
│                                                          │"                                                         │                          │
├──────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────┼──────────────────────────┤
│"Muon Physics: A Pillar of the Standard Model"            │"Electroweak Radiative Corrections to Muon Capture"       │2                         │
└──────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────┴──────────────────────────┘
- From the cocitation and bibliographic coupling tables, we can see that the most cocitation and bibliographic coupling pairs are related to each other. On the one hand, the number of cocitation and bibliographic coupling pairs is very low compared to the number of papers. This is because not all papers are cited by all other papers and vice versa which is common in citation networks.

### 3.3 Nodes metrics
1. The paper that has the highest degree (using neuler):
    ![Graph Screenshot](pictures/Screenshot%202024-10-22%195153.png)
    - The result show that a paper with title "Moriond QCD 2007 - Theory Summary" has the most informaiton about other papers with 5 citations.
2. The paper that has the highest betweenness centrality (using neuler):
    ![Graph Screenshot](pictures/Screenshot%202024-10-22%195813.png)
    - The result show that a paper with title "Moriond QCD 2007 - Theory Summary" has the highest betweenness centrality with the score of 24. This means that this paper is the most important paper in the network since it has the most shortest paths between other papers.
3. The paper that has the highest closeness centrality (using neuler):
    ![Graph Screenshot](pictures/Screenshot%202024-10-22%200533.png)
    - The result show that all papers have the same closeness score of 1. This means that each paper cites or is cited by all other papers in the network. This is common in citation networks since all papers are connected to each other through citations.
4. The paper that has the highest eigenvector centrality (using neuler):
    ![Graph Screenshot](pictures/Screenshot%202024-10-22%201226.png)
    - The result show that the papers with the following tittles "Marginal Solutions for the Superstring", "Analytic solutions for marginal deformations in open superstring field theory", "Direct extraction of one-loop integral coefficients", "Numerical Evaluation of Six-Photon Amplitudes" have the highest eigenvector centrality with the score of 0.45. This means that these papers are the most influence and prestige papers in the network since they are cited by other important papers.
5. Papers with highest custering coefficient (using neuler):
    ![Graph Screenshot](pictures/Screenshot%202024-10-22%203136.png)
    ![Graph Screenshot](pictures/Screenshot%202024-10-22%203245.png)
    ![Graph Screenshot](pictures/Screenshot%202024-10-22%203319.png)
    - The result show that there are 30 papers with the highest clustering coefficient of 1. This means that these papers are in the same cluster and they are connected to each other through citations. This is common in citation networks since papers in the same categories are usually cited by each other.

## 4. Limitaion:
    - The limitation of this analysis is that the neu4j graph is not big enough to fully show 4000 papers which mean that the result may not be accurate. In addition, the analysis is only based on the data in the graph database, so it may not be able to show the full picture of the citation network.

## 5. Conclustion:
    - In conclusion, by using many data analysis techniques and tool, we can analyze the citation network to find the most important papers, the most popular categories, the most cocitation and bibliographic coupling pairs, and the most influence papers. This analysis can help us to understand the structure of the citation network and the relationship between papers in the network. However, the limitation of the analysis is that the graph database is not big enough to fully show the citation network and we may not be able to get the full picture of the network. In the further work, we will remodify the althorithm to collect datas that able to show the full picture of the network.
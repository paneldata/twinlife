---
name: twinlife
label: TwinLife
config:
    variables:
        label-table: True
---

# TwinLife

## Citation

* **Title:** TwinLife  - A genetically informative, longitudinal study about the development of social    
    inequality
* **Principle Investigators:** Prof. Dr. Martin Diewald (martin.diewald[at]uni-bielefeld.de);    
    Prof. Dr. Rainer Riemann (rainer.riemann[at]uni-bielefeld.de);    
    Prof. Dr. Frank M. Spinath (f.spinath[at]mx.uni-saarland.de)
* **URL:** [http://www.twin-life.de/](http://www.twin-life.de/)

Please cite both the dataset (Diewald et al., 2019: [http://doi.org/doi:10.4232/1.13208](http://doi.org/doi:10.4232/1.13208)) and the reference paper (Hahn et al., 2016: 
[https://doi.org/10.1017/thg.2016.76](https://doi.org/10.1017/thg.2016.76)).

## Study info

TwinLife is a 12-year representative behavior genetic study investigating the emergence and development of social inequalities over the life course.

The long-term project began in 2014 and surveys more than 4,000 pairs of twins and their families in different stages of life on a yearly basis. All of the subjects reside in Germany. 
Not only social, but also genetic mechanisms as well as covariations and interactions between these two factors can be examined with the help of identical and fraternal same-sex twins.

In order to document the individual development of different aspects it is important to examine the families extensively over the course of several years. Six important contextual domains 
are focused on: 1.) Education and academic performance / skill development, 2.) career and labor market attainment, 3.) integration and participation in social, cultural and political life, 
4.) quality of life and perceived capabilities, 5.) physical and psychological health and 6.) behavioral problems and deviant behavior.

In order to take a close look at the development of social inequalities, TwinLife does not only examine different etiological factors, but also different indicators of personal and social 
success and failure respectively. On part of the conditional factors genetic disposition as well as aspects of the environment that the children and adolescents are living in are considered. 
On part of the consequences not only objective but also subjective information is observed. Children are born into an environment which influences them, but on the other hand they react and 
interact differently depending on their individual characteristics and thereby shape their environment. To allow for an accurate examination of the reciprocal processes by which individual 
dispositions and environmental conditions influence each other, data on the illustrated characteristics will be collected over a period of twelve years.

In the following, the contents of the TwinLife Data are described in more detail by the life domains outlined above:

**1. Skill formation and education**

1.1 Educational success

- School report; if not available: supplementary questions
- Current school marks or rather marks of highest graduation 
          
1.2 Intelligence

- Subtests Matrices, Series, and Classification
- Subtests Matrices, Series, Reasoning, Classification

1.3 Cognitive development   
 
- General information derived from "U-Heft"; if not available: supplementary questions
- Interviewer rating on task orientation and oral skills following intelligence test
- Tutoring and homework help/special educational treatment/attendance of special school
- Competence rating of social skills, oral skills, concentration ability, communications skills, mathematic ability, general knowledge

1.4 Media use

- Frequency and duration of media use (e.g., Internet, Laptop, TV, games console etc.)

1.5 Academic self-concept

- Verbal and spatial skills, spatial and general
- Verbal, mathematic, and general academic ability
- Perceived competence

1.6 Intrinsic motivation, learning motivation, achievement motivation

- Educational values of German, maths, and school in general
- Learning and achievement motivation in German, maths, and school in general
- Learning goals

1.7 Self-efficacy

- General self-efficacy

1.8	Self-esteem

- General self-esteem

1.9	Self-regulation

- Consistency of interest, self-control

1.10 Personality

- Neuroticism, extraversion, openness, agreeableness, conscientiousness


**2. Career and labor market attainment**

2.1	Employment status

- Current employment status/changes regarding employment

2.2	Education

- History of education
- Education and qualification
- Educational and career aspirations

2.3	Information on current job

- Perceived job security and satisfaction
- Wages/income/welfare dependency

2.4 Economic preferences

- Risk aversion


**3. Integration and participation in social, cultural, and political life**

3.1 Migration background and citizenship

- Current status of citizenship and changes of citizenship
- Migration

3.2 Discrimination

- Experiences with discrimination

3.3 Social participation

- Frequency of attendance in sports clubs, theatre, music groups or volunteer organizations

3.4 Social networks

- Social capital of individuals, e.g., close friends, frequency of social contacts
- Loneliness

3.5 Political participation

- Interest in politics, political preferences, voting behavior

3.6 Religion

- Religious affiliation, church attendance, religiosity/spirituality


**4.	Subjective perceptions of quality of life**

4.1 Life satisfaction

- Global life satisfaction 
- Domain satisfaction (health, work life, family life, leisure time, school, romantic relationship, friendships, income)
- Satisfaction with sibling relationship


**5. Physical and psychological health**

5.1 Health

- Current subjective health
- Current subjective health
- Health behavior 

5.2 Measures of height and weight

- Measure of actual height and/or weight, if not remembered, scale measure during INTH


**6. Deviant behavior and behavioral problems**

6.1 Internalizing

- Emotional symptoms, problems with peers, social difficulties

6.2 Externalizing

- Hyperactivity, attention problems, behavioral difficulties

6.3 Deviant and delinquent behavior

- Occurrence and frequency of problematic behavior (e.g., fare evasion, skip school, drug use, thieving, property damage, physical assault)
- Supplementary questions on e.g., impulse control and rebellious behavior
- Short version of deviant/delinquent behavior measure


**7. Demographics**

7.1 Information on household

- Household questionnaire (persons in the household, household grid, type of dwelling, income), information on assets


**8. Environment**

8.1 Activities with children

- Occurrence and frequency of e.g., singing and making music together; story time; doing sports; cultural activities

8.2 Nursery

- Detailed information on nursery and daycare institutions

8.3 Grand-parents

- Relationship: contact frequency, quality of relationship

8.4 Parenting style

- Monitoring, warmth, rules, negative communication, control (child and parent report on parental behavior)

8.5 Quality of home environment

- Characteristics of a chaotic, disorganized, and hurried home
- Interviewer ratings on the home environment (household)

8.6 Involvement

- Autonomy, structure, control, emotional support

8.7 Sibling relationship

- Warmth, conflict, rivalry of sibling relationship
- Affection, hostility, rivalry of sibling relationship


**9. Zygosity and twin specific items**

9.1 Zygosity

- Ratings of physical twin similarity in childhood (e.g., eye color, hair structure, time of getting first teeth)

9.2 Twin specific questions

- E.g., same or different clothing, confusion of the twins, undertakings with twins


The data delivery consists of a certain number of data files in different data formats:

- One master data set (ZA6701_master_v$): Includes information on the gross sample, such as consistency checked, time stable variables (sex, year of birth, relation to twins, zygosity) 
and wave-specific variables (person type, response status, family composition) about all individuals included in TwinLife in each wave
- One data file in person-wave-format (‘long format’; ZA6701_person_v$): Each surveyed person has one data row for each survey wave. The data set includes data of the personal interviews 
as well as information about the household. Wave identifier is the variable wid.
- One data set for each survey wave in family format (‘wide format’; ZA6701_family_wave_x_v$), in which each family has one data row (information of each participating person in the family 
is stored in separate variables/columns). These data sets are restructured from the person-wave-format and therefore include the same data.
- One data set (ZA6701_zygosity_v$) that includes the information of the twin zygosity assessment
- Two data sets (one in family and person format, respectively; e.g. ZA6701_person_add_scales_v$ in the person-wave-format) containing additionally generated scales, as well as age- and 
sex-corrected residuals of these scales (e.g. personality and parenting style)
- One data set in which the survey mode for each variable on the individual level (ZA6701_mode_v$) is documented

The data are adjusted for filter errors, i.e. data that was collected due to wrong filter conditions has been overwritten.

## Method

The TwinLife panel combines a sequential cohort-design with an extended twin family-design (ETFD). The related surveys are conducted yearly, whereat the mode alternates between face-to-face at 
home, including some tests, and telephone interviews. Parts of the face-to-face surveys are conducted in parallel modes, i.e., as computer assisted or paper-and-pencil self-interviews.

The sequential cohort-design comprises four cohorts: The youngest twins in cohort 1 (birth years 2009 and 2010) are about 5 years of age at the time of the first survey in 2014 and 2015. The 
oldest twins in cohort 4 (birth years 1990 to 1993) are about 31 to 32 years of age at the time of the last survey in 2022 and 2023. The twins in cohorts 2 and 3 are born in the years 2003 to 
2004 and 1997 to 1998, respectively. This design enables the TwinLife panel to cover an age range between 5 and 32 years with a data collection phase of 10 years. This age range covers important 
life-course transitions from school entry to the labor market entry phase as well as critical life stages for mating and family formation.

As part of the ETFD, in addition to the twins themselves the biological and if applicable social parents as well as the sibling that is closest in age to the twins are surveyed. Moreover, the 
partners of adult twins are included as well. This family perspective enables comparisons regarding different degrees of genetic similarity, and it is important to analyze the manifold influences 
of the family environment on the development of the twins in greater detail.

**Geographic Coverage:** Germany
 
**Universe:** Twins and their families (Extended Twin Family Design, ETFD): Monozygotic and dizygotic same-sex twin pairs born in the following years: 1.) 1990 and 1991, 2.) 1997, 3.) 2003 and 
4.) 2009 (4 birth cohorts)

plus at least one biological parent

(+ if possible the other biological parent, step-parent(-s), one sibling and the twins' partners)
 
**Selection Method:** Twin families are drawn from local resident registers in communities with at least 5,000 inhabitants in Germany. The twin families are recognized as such if two same-sex 
people with the same date of birth lived in the same household. Then, it was checked whether the selected persons were twins indeed.
 
**Mode of Data Collection:** Face-to-Face interviews: Household interviews with the family via three different interview modes (CAPI, CASI, Paper-and-Pencil) plus cognitive tests, scans/photos 
of certificates and children's health record books; interviews with family members living outside the interviewed households by two modes (CAWI, Paper-and-pencil).
CATI interviews: Telephone interview with one family member (from second CATI wave onwards; before: telephone interview with each family member above the age of 10 that participated in the 
preceding Face-to-Face wave)
 
**Survey institute:** TNS Infratest / Kantar TNS (first Face-to-Face household survey, parts of the first telephone survey); infas Institut für angewandte Sozialwissenschaft 
(parts of the first telephone survey) 
 
**Date of Collection:**

10/01/2014 to 05/31/2015 (Face-to-Face 1a)

10/01/2015 to 04/30/2016 (Face-to-Face 1b, CATI 1a)

10/01/2016 to 04/30/2017 (CATI 1b)

## Data access 

GESIS Data Catalogue: [https://dbk.gesis.org/dbksearch/index.asp](https://dbk.gesis.org/dbksearch/index.asp)

## Data description

For a description of the structure of the TwinLife sample see the TwinLife Technical Report 03, for the method report of the first wave see the TwinLife Technical Report 05 at 
[https://www.twin-life.de/en/twinlife-technical-report-series](https://www.twin-life.de/en/twinlife-technical-report-series).

## Study units

Number of Units:
19163 individuals, 4097 families
 
Number of Variables:

3046 (person format), 87 (zygosity data set) 

8178 (family format wave F2F1; not documented at paneldata.org), 3026 (family format wave CATI1; not documented at paneldata.org)

## Other material and Notes

Availability Class:
C (Data and documents are only released for academic research and teaching after the data depositor’s written authorization. For this purpose the Data Archive obtains a written permission 
with specification of the user and the analysis intention.)
 
Further Remarks:

TwinLife website: [http://www.twin-life.de/en](http://www.twin-life.de/en)

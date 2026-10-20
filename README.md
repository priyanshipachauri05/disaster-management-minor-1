## Disaster Management and Response Support System

### Overview

Natural disasters can cause significant damage to infrastructure and put human lives at risk. Assessing the extent of damage and identifying areas that require immediate assistance are important steps in disaster response.

This project aims to develop a disaster-management platform that uses the satellite images analysis, remote sensing and geospatial information to support damage assessment and rescue planning.

The goal is to explore how computational techniques can help analyze disaster-affected areas, identify changes in infrastructure, and provide useful information for disaster-response teams.

### Research Motivation

Natural disaster can affect large areas, making it difficult to assess damage and identify where assistance may be needed most. Remote sensing provides a way to observe affected regions, while computer vision could help extract useful information from imagery.

However, detecting damage from satellite images is not straightforward. Results can depend on image resolution, the availability of pre-disaster imagery and the difference between training data and real-world imagery.

This project investigates these challenges through small experiments before moving towards the integrating the individual components into a disaster-response support system.

### Project Objectives

The project focuses on five main objectives:

1. Disaster Assessment: Explore methods to identify disaster types, estimates severity, and assess the affected population.
2. Damage Detection: Compare pre-disaster and post-disaster imagery to identify changes and estimate the extent of damage.
3. Rescue Prioritisation: Explore ways to priorities affected areas using damage estimates, possible human presence, accessibility and available resources.
4. Historical Data Analysis: Investigate how historical disaster information can support preparedness and future disaster planning.

### Current Experimental Work

Development is currently focused on evaluating individual methods and understanding their limitations before integrating them into the larger system.

The experimental works include:

o Exploring image-based change detection for comparing disaster imagery.

o Evaluating building-damage classification using xBD dataset.

o Analysing class distribution.

o Using density-based heatmaps to train the first CNN model and identifying the architectural        limitation of the model.

Detailed experiment configurations, results, and observations will be documented alongside the relevant code.

### Technologies 

o Python for experimental implementation and analysis.

o Computer Vision and Image processing for image comparison and damage assessment.

o Machine learning and Deep learning.

o QGIS for working with geographic information and visualising spatial results.


### Planned work

o Evaluate suitable datasets for different disaster types.

o Develop and test image-analysis and damage-detection methods.

o Explore geospatial visualization of the affected areas.

o Investigate methods for rescue prioritization.

o Integrate the components into a disaster-response support information.

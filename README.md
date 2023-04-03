
# **Report is located in task.ipynb**



# Coding assessment for Clinical Computational Cancer Genomics
## Author: Ian Snyder 
## Instructor/Lead: Dr. Saud AlDubayan


**Assigned: April 1, 2023**
**Due: April 10, 2023**

## Overall question: Can you discover any mutations that are associated with treatment response??

## Task
Can you discover any mutations that are associated with treatment response?

## Methods 
Methods implemented, detailed, and displayed in task.ipynb. 

## Figures 

### Most Enriched Genes 
![Unknown](https://user-images.githubusercontent.com/58576523/229612553-5c3033f5-0dcf-4310-bcba-ec2c5a0aaf24.png)

### Most Enriched Genes: seperated by response group
![Unknown2](https://user-images.githubusercontent.com/58576523/229612962-3abaa8f4-e4fa-4fe1-86fd-9592b7e82fcb.png)

### Total Occurance of Enriched Genes as a scatter plot
![Unknown-2](https://user-images.githubusercontent.com/58576523/229613129-4023c4ae-d6d0-45f8-bf17-0dac297804e8.png)

### Total Occurance of Enriched Genes as a bar graph
![Unknown-3](https://user-images.githubusercontent.com/58576523/229613214-2a70a48e-8a3d-44d0-93cf-5d2be474622a.png)

### Mutant vs Wildytype
![Unknown-4](https://user-images.githubusercontent.com/58576523/229613333-3945d1d5-7a07-4b5a-ab3e-82541920dcdf.png)


## Conclusion
The results from this analysis suggest there are genes associated with treatment response, specifically the gene KMT2C. However, a sample size of 50 is not large enough to draw any major conclusions, but this study suggests it could be worth investigating further. One of the big issues with small sample sizes is that individuals who dont represent the true population can influence the data dramatically leading to false conclusions. In this study specifically, the frequency of the most enriched gene KMT2C was 20. Patient-38 had 12 mutations on this gene specifically, meaning this indivudal skewed the data tremendously. We have no idea what stage of cancer they were in, or what previous exposures they had that may promoted mutations at that gene. A larger dataset would allow a much more compelling analysis, larger data decreases the individuals weight in statistical analysis. It is worth noting, even when only considering unique genes per patient, the gene KMT2C was still identified as the clear most enriched gene.
Overall, this study suggests the gene KMT2C may be associated with treatment response. However, it would be unresponsible to ignore the factors mentioned above before asserting the claim as conclusive.

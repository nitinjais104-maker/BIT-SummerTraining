0. Dataset Load Karo
1. Dataset ko ek DataFrame mein load karo and pehli kuch rows dekho.
2. Explore
    - Kitne rows? kitne columns? 
    - kitne missing values ? 
    - column naam aur data types ? 
3. Visualize 
    - Do scatter plots banao: 
        - 1. Annual Income Vs Spending Score 
        - 2. Age Vs Spending Score
4. Select Features
    - Decide karo : clustering k liye konsa columns use krenge

5. Find Best K
- Elbow Method use krk dekho best K kya hai ?

6. Train 
- Ek K-Means model train karo ( apne chune hue K pe)

7. Predict 
- Clusters predict karo aur unhe ek naye column "Cluster" mein store karo

8. Visualize Clusters:
- Clusters ko centroids ke saath plot karo 
- har goup alag color , centroids alag marker 


<!-- Check your metrics  -->
## from sklearn.metrics import silhouette_score


9. Business Insights 
- 1. kaunsa CLuster sabse zayada kharch karta hai ? 
- 2. kaunsa cluster sabse zyada kamata hai ? 
- 3. kis cluster ko discount dena chahiye ? Kyun? 
- 4. Kis cluster ko premium memebership dena chahiye ? kyun ? 
- 5. kis cluster ko advertisement target karna chahiye ? Kyu ? 
0. Dataset Load Krna hai 
1. Dataset ko ek DataFrame mein Load krna hai and starting ki kuch rows dekhna hai 
2. Explore -> 
        - Kitne rows? kitne columnsc?
        - Kitni missing values ? 
        - Columns name and datatype kya hai ?
3. Visualize: - 2 scatter plots
        - 1. Annual Income Vs Spending Score 
        - 2. Age vs Spendibg Score
4. Select Feature (DATA)  
- Decide Karo : Clustering k liye konsa columns use krenge ? 

5. Find BEST K
- Elbow Method use krk best L (no. of clusters) nikaalo.

6. Train
- Ek K_Means model train karo ( aapne jo k choose kia hai )

7. Predict 
Clusters predict karo aur unhe ek naye column "CLUSTER" mein store karo 

8. Visualize Clusters
- Clusters ko 'centroids k sath' plot karo - har group alag color, cnetorids alag marker

9. Business Insights 
- 1. kaunsa CLuster sabse zayada kharch karta hai ? 
- 2. kaunsa cluster sabse zyada kamata hai ? 
- 3. kis cluster ko discount dena chahiye ? Kyun? 
- 4. Kis cluster ko premium memebership dena chahiye ? kyun ? 
- 5. kis cluster ko advertisement target karna chahiye ? Kyu ? 

<!-- Check your metrics  -->
## from sklearn.metrics import silhouette_score



## joblib - model train hoke download -> .pkl
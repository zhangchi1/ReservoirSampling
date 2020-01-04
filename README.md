# ReservoirSampling
sample k elements with equal probability from n numbers
## 1. Simple random sampling method with a finit-size list of elements: N (N is known).
<br>
Select each element in the sample set S, with probability of x <img src="https://latex.codecogs.com/svg.latex?\Large&space;x=\frac{K-|S|}{N-i}=\frac{K}{N}" /> at each step i

<br>

## 2. My Reservoir Sampling algorithm (N is usually unknown, where data is too large to load into the memory).

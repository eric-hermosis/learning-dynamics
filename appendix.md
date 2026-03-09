## Derivation of Learning Equations

We begin with the equations describing the system without temperature coupling, expressed in terms of the intensive variables $\mathbf{Y}$:

$$
\begin{aligned}
-h \frac{dw^{i}}{dt} = k\{w^{i}, H\} = k\frac{\partial H}{\partial Y_{i}} \qquad -h\frac{dY_{i}}{dt} = k\{Y_{i}, H  \} = -k\frac{\partial H}{\partial w^{i}}
\\
\\
-h \frac{dU}{dt} = k\frac{\partial H}{\partial \beta} \qquad -h\frac{d\beta}{dt} = -k\frac{\partial H}{\partial U}
\end{aligned}
$$

Next, we introduce the coupling between the intensive parameters and temperature:

$$
\mathbf{Y} = \beta \mathbf{X}.
$$

### Evolution of the Weights

Since the Hamiltonian can be expressed in terms of the variables $\mathbf{X}$ after the change of coordinates, the derivative with respect to $Y_i$ must be evaluated using the chain rule: 

$$
\frac{\partial H}{\partial Y_{i}} = \sum_j \frac{\partial H}{\partial X_{j}} \frac{\partial X_{j}}{\partial Y_{i}}.
$$

From the relation:

$$
X_j = \frac{Y_j}{\beta},
$$

we obtain:

$$
\frac{\partial X_j}{\partial Y_i} = \frac{1}{\beta}\delta_{ij},
$$

where $\delta_{ij}$ denotes the Kronecker delta. Consequently, the sum collapses to a single term:

$$
\frac{\partial H}{\partial Y_{i}} = \frac{1}{\beta} \frac{\partial H}{\partial X_{i}}.
$$

Substituting into Hamilton’s equation gives the weight evolution equation:

$$
-h\frac{dw^{i}}{dt} = \frac{k}{\beta} \frac{\partial H}{\partial X_{i}}.
$$

### Evolution of the Energy Moments

Using the Leibniz rule for Poisson brackets, the bracket involving $Y_i$ becomes:

$$
\{Y_{i}, H\} = \{\beta X_{i}, H\} = \beta\{X_{i}, H\} + X_{i}\{\beta, H\}.
$$

From the uncoupled system we have:

$$
\{Y_{i}, H \} = -\frac{\partial H}{\partial w^{i}} \qquad  \{\beta, H\} = -\frac{\partial H}{\partial U},
$$

substituting these expressions yields:

$$
-\frac{\partial H}{\partial w^{i}} = \beta \{X_{i}, H\} - X_{i} \frac{\partial H}{\partial U},
$$

solving for the Poisson bracket gives

$$
\{X_{i}, H\} = -\frac{1}{\beta}\frac{\partial H}{\partial w^{i}} + \frac{X_{i}}{\beta} \frac{\partial H}{\partial U},
$$

substituting into Hamilton’s equation then gives the evolution equation for the momenta:

$$
-h\frac{dX_{i}}{dt} = k\{X_{i}, H\} = -\frac{k}{\beta}\frac{\partial H}{\partial w^{i}} + \frac{kX_{i}}{\beta} \frac{\partial H}{\partial U}.
$$

### Evolution of Internal Energy

To derive the equation governing the evolution of the internal energy, we must account for the fact that the Hamiltonian may be expressed in terms of either $\mathbf{Y}$ or $\mathbf{X}$. Using the thermodynamic identity

$$
\left(\frac{\partial H}{\partial \beta} \right)_{\mathbf{Y}} =  
\left(\frac{\partial H}{\partial \beta} \right)_{\mathbf{X}} + \sum_{j} \left(\frac{\partial H}{\partial X_{j}} \right)_{\beta, X_{i \neq j}} \left(\frac{\partial X_{j}}{\partial \beta} \right)_{\mathbf{Y}},
$$
 
where the subscripts indicate which parameters are held constant. This notation is common in thermodynamics and was previously omitted, as we specified at each step the symplectic form under consideration.

Next, we compute the partial derivative of the momenta with respect to the parameter $\beta$.  From the coupling relation:

$$
X_{i}  = \frac{Y_{i}}{\beta},
$$

it follows that:

$$
\frac{\partial X_{i}}{\partial \beta} = -\frac{1}{\beta^2} Y_{i} = -\frac{1}{\beta} X_{i}.
$$

Substituting into the identity yields

$$
-h\frac{dU}{dt} = k\frac{\partial H}{\partial \beta} - \frac{1}{\beta} \sum_{j} \frac{\partial H}{\partial X_{j}}X_{j}.
$$

### Evolution of the Thermal Parameter

The remaining equation governing the evolution of $\beta$,

$$
-h\frac{d\beta}{dt} = -k\frac{\partial H}{\partial U},
$$

remains unchanged, since the internal energy $U$ is not coupled to the variables $\mathbf{X}$ in the same manner as $\beta$.
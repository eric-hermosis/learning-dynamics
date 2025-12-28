## Derivation of learning equations

The equations for the system without temperature coupling, described by the variables $\mathbf{Y}$, are:

$$
-h \frac{dw^{i}}{dt} = k\{w^{i}, H\} = k\frac{\partial H}{\partial Y_{i}} \qquad -\frac{dY_{i}}{dt} = k\{Y_{i}, H  \} = -k\frac{\partial H}{\partial w^{i}}
$$

$$
-\frac{dU}{dt} = k\frac{\partial H}{\partial \beta} \qquad -h\frac{d\beta}{dt} = -k\frac{\partial H}{\partial U}
$$

Let now derive the equations with the coupling $\mathbf{Y} = \beta \mathbf{X}$. Using the Leibniz rule for the bracket containing the coordinates of $\mathbf{Y}$, for a Hamiltonian $H$, we have:

$$
\{Y_{i}, H\} = \{\beta X_{i}, H\} = \beta\{X_{i}, H\} + X_{i}\{\beta, H\}
$$

Given that:

$$
\{Y_{i}, H  \} = -\frac{\partial H}{\partial w^{i}} \qquad  \{\beta, H\} = -\frac{\partial H}{\partial U}
$$

We can substitute these values to obtain the Poisson brackets of the system in terms of the momenta $\mathbf{X}$:

$$
-\frac{\partial H}{\partial w^{i}} = \beta \{X_{i}, H\} - X_{i} \frac{\partial H}{\partial U} \Rightarrow \{X_{i}, H\} = -\frac{1}{\beta}\frac{\partial H}{\partial w^{i}} + \frac{X_{i}}{\beta} \frac{\partial H}{\partial U}
$$

We then recover the second proposed equation for evolution of momentum:

$$
-h\frac{dX_{i}}{dt} = k\{X_{i}, H\} = -\frac{k}{\beta}\frac{\partial H}{\partial w^{i}} + \frac{kX_{i}}{\beta} \frac{\partial H}{\partial U}
$$

To reconcile the evolution of the internal energy with the third proposed equation, we recall the following thermodynamic identity:

$$
\left(\frac{\partial H}{\partial \beta} \right)_{\mathbf{Y}} =  
\left(\frac{\partial H}{\partial \beta} \right)_{\mathbf{X}} + \sum_{j} \left(\frac{\partial H}{\partial X_{j}} \right)_{\beta, X_{i \neq j}} \left(\frac{\partial X_{j}}{\partial \beta} \right)_{\mathbf{Y}}
$$

The subscripts indicate which parameters are held constant. This notation is common in thermodynamics and was previously omitted, as we specified at each step the symplectic form under consideration. Next, we find the partial derivative of the momentum with respect to the parameter $\beta$. From the coupling relation:

$$
X_{i}  = \frac{Y_{i}}{\beta} \Rightarrow \frac{\partial X_{i}}{\partial \beta} = -\frac{1}{\beta^2} Y_{i} = -\frac{1}{\beta} X_{i}
$$

We can then obtain the evolution of the internal energy:

$$
-h\frac{dU}{dt} = k\frac{\partial H}{\partial \beta} - \frac{1}{\beta} \sum_{j} \frac{\partial H}{\partial X_{j}}X_{j}
$$

For the weight–momentum brackets, we note that:

$$
\frac{\partial H}{\partial Y_{i}} = \frac{\partial H}{\partial X_{i}} \frac{\partial X_{i}}{\partial Y_{i}} = \frac{1}{\beta} \frac{\partial H}{\partial X_{i}}
$$

Thus:

$$
-h\frac{dw^{i}}{dt} = \frac{k}{\beta} \frac{\partial H}{\partial X_{i}}
$$

Finally, the equation describing changes of $H$ in the direction $\partial/\partial U$ remains unchanged, since the variable $U$ is not coupled in the same manner as $\beta$.
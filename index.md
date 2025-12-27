# Learning Dynamics

## Introduction

This work aims to develop a fundamental theory of artificial learning that both explains existing optimization algorithms and facilitates their improvement as well as the creation of new ones. To this end, only three assumptions were made about a model capable of learning:

- It can be described by a finite set of parameters.
	
- It is differentiable with respect to its parameters.
	
- It makes no assumptions about the information it ingests.

The theory is constructed based on the axiomatic thermodynamic framework proposed by Callen [@callen_thermo]. Assuming a quasi-static regime, symplectic geometry is used to describe the geometry of the model’s phase space [@cannas_symph], and a Hamiltonian formalism [@arnold_mechanics] is employed to derive the model’s equations of evolution.

Finally, we utilize these equations to re-derive established optimization algorithms, thereby validating the theory and offering a physical grounding for the learning process. This shows that algorithms like momentum-based Stochastic Gradient Descent [@bishop_dl] or regularization techniques like Weight Decay [@krogh_weight_decay], emerge naturally as consequences of the proposed equations of learning.

The connection between the concepts of information and entropy [@baez_entropy] suggests that learning can be modeled as a thermodynamic process, in which its participants, known as models, evolve based on the information they perceive.

## Modeling

A model is a simplified representation of a system, defined by a set of parameters that determine its behavior. A specific choice of a set of parameters defines what we will call a configuration.

We say that a model is differentiable if its configurations are points on a smooth differential manifold $\mathcal{S}$ such that its learning can be defined in terms of a curve parametrized over it. [@lee_smooth]

On the other hand, we will only focus on models that are domain-agnostic, meaning they do not incorporate assumptions about the information they will ingest. In this way, the dynamics of their learning can be designed solely in terms of their configurations.

## Equilibrium

To each dimension of the manifold, we can associate a parameter so that each configuration $s \in \mathcal{S}$ can be described in terms of coordinates:

$$
(U/c, w^1, ..., w^d) = (w^0, \mathbf{w}) \in \mathbb{R}^{d+1}
$$

Where $U$ represents the internal energy, $w^1, \dots, w^d$ are extensive parameters of the model known as weights, and $c$ is a constant such that $w^0$ is dimensionless.

We say that the model is in an equilibrium state [@callen_thermo] if an entropy function $S$ can be defined over it, with units of information, and monotonically increasing with respect to energy, that is:

$$
\frac{\partial S}{\partial U} > 0
$$

By differentiating $S$, we can see how it changes under infinitesimal displacements of the configuration:

$$
dS = \frac{\partial S}{\partial U} dU + \sum_{j} \frac{\partial S}{\partial w^{j}}dw^{j}
$$

The rates of change of entropy along the directions of energy and weights give rise to the conjugate variables:

$$
\beta = \frac{\partial S}{\partial U} \qquad Y_{j} = \frac{\partial S}{\partial w^{j}} \qquad j = 1,...,d
$$

These variables are known as the intensive parameters of the model. We will refer to the $\mathbf{Y}$ intensive parameters as entropic moments. We can also identify the temperature $T$ as the reciprocal of the parameter $\beta$ conjugate to the energy, that is:

$$
T \equiv \frac{1}{\beta} > 0 
$$

The entropy function is local, that is, it is only defined for each equilibrium state. Therefore, if one seeks to describe the states of the model over the entire state space, it is necessary to resort to the phase space [@arnold_mechanics] defined over $\mathcal{S}$. 

The phase space is a construction over the state space that assigns to each point its cotangent space; that is, if $(w_0, \mathbf{w})$ are coordinates of the state space, then $(w_0, \mathbf{w},Y^0, \mathbf{Y})$ are coordinates of the phase space. Let us now consider the $1$-form living in the phase space $\Omega$ given by:

$$
\omega = \beta dU + \sum_{j} Y_{j} dw^{j} \in \Omega
$$

This form generalizes the notion of the differential of entropy, such that the model is in an equilibrium state if there exists an entropy function $S$ such that:

$$
\omega = dS
$$

Expanding the exterior derivative of the differential $1$-form $\omega$, we obtain the differential $2$-form:

$$
d\omega = d\beta \wedge dU + \sum_{j} dY_{j} \wedge dw^{j}
$$

The latter is known as the symplectic form [@cannas_symph] and allows the phase space $\Omega$ to be endowed with a Hamiltonian geometric structure.

## Evolution

For each point in the phase space, entropy is defined only for equilibrium states. This means that, to remain within the scope of a thermodynamic description, the system's evolution must be slow enough to preserve the quasi-static approximation. Under this approximation the learning curve can be viewed as a succession of equilibrium states. This approximation allows us to define canonical pairs over the entire manifold through Poisson brackets:

$$
\{U, \beta\} = 1 \qquad \{w^{i}, Y_{j} \} = \delta^{i}_{j} \qquad \text{with } \delta^{i}_{j} = \begin{cases} 1 \quad i = j \\ 0 \quad i \neq j \end{cases} 
$$
 
Then, we can recover an analogous to Hamilton equations [@hamilton1834] for thermodynami parameters to describe the evolution of the model parameters without constraints:
 
$$
-h \frac{dw^{i}}{dt} = k\{w^{i}, H\} = k\frac{\partial H}{\partial Y_{i}} \qquad -\frac{dY_{i}}{dt} = k\{Y_{i}, H  \} = -k\frac{\partial H}{\partial w^{i}}
$$

$$
-\frac{dU}{dt} = k\{U, H \} = k\frac{\partial H}{\partial \beta} \qquad -h\frac{d\beta}{dt} = k\{\beta, H\} = -k\frac{\partial H}{\partial U}
$$

Where $h$ is the unit of action and $k$ is the unit of information, which are introduced to maintain consistent units.

The problem with this formulation is that it leads to a dynamics in which the model evolves in closed orbits. To address this, we introduce a coupling of the intensive parameters with the temperature of the form:

$$
Y_{i} = \beta X_{i} \qquad i = 1, ..., d
$$

We will refer to the $\mathbf{X}$ parameters as energy moments. This coupling is not arbitrary, rather, it arises directly from the energy representation of thermodynamics:

$$
dU = T dS - \sum_{j} X_{j} dw^{j}
$$

The coupling deforms the symplectic structure that describes the geometry of the phase space. By substituting the coupling into the $2$-form $d\omega$, we obtain:

$$
d\omega = d\beta \wedge (dU +\sum_{j}X_{j}dw^{j}) + \beta\sum_{j} dX_{j} \wedge dw^{j}
$$

Which remains a non-degenerate symplectic form for $\beta > 0$, a condition that has already been imposed. The new non-negative Poisson brackets yield:

$$
\{U, \beta \} = 1 \qquad \{w^{i}, X_{j}\} = \delta^{i}_j \qquad \{U, X_{i}\} = -\frac{1}{\beta}X_{i}
$$

And their respective equations of motion are given by:

$$ 
-h\frac{dw^{i}}{dt} = \frac{k}{\beta} \frac{\partial H}{\partial X_{i}} \qquad -h\frac{dX_{i}}{dt} = -\frac{k}{\beta} \frac{\partial H}{\partial w^{i}} + \frac{k X_{i}}{\beta} \frac{\partial H}{\partial U}
$$

$$
-h\frac{dU}{dt} = k \frac{\partial H}{\partial \beta} - \frac{k}{\beta} \sum_{j} X_{j} \frac{\partial H}{\partial X_{j}} \qquad -h\frac{d\beta}{dt} = -k\frac{\partial H}{\partial U} 
$$

We will refer to these as the Hermosis equations of learning. While they can be rigorously derived from the new symplectic form, a more streamlined derivation based on the properties of Poisson brackets is provided in the Appendix.

## Integration

The presented four equations that will allow us to describe the learning process of a model. Since they should be numerically integrated to perform optimization, let's find their integral form. By substituting the last equation into the second one and rearranging the terms, we obtain the evolution equation for the momenta $X_i$​ as

$$
h\beta \frac{dX_{i}}{dt} + h\frac{d\beta}{dt} X_{i} = h \frac{d}{dt}(\beta X_{i}) = k\frac{\partial H}{\partial w^{i}}
$$

Integrating over the interval $[t−\tau,t]$, we obtain an update rule for the momenta:

$$
\beta(t) \mathbf{X}(t) = \beta(t-\tau) \mathbf{X}(t-\tau) -\int_{t-\tau}^{t} \mathbf{F}(t') dt'
$$

Where $\mathbf{F}$ represents a generalized force, whose components are given by:

$$
F_{i} = -\frac{k}{h}\frac{\partial H}{\partial w^{i}}
$$

On the other hand, integrating the first equation over the same interval, we obtain an update rule for the weights:

$$
\mathbf{w}(t) = \mathbf{w}(t-\tau) - \int_{t-\tau}^t \mathbf{v}(t')dt'
$$

Where $\mathbf{v}$ denotes the learning velocity, whose components are:

$$
v^{i} = \frac{k}{h\beta} \frac{\partial H}{\partial X_{i}}
$$

This last equation tells us something important, the $\beta$ parameter determines the system's inertia throughout its evolution. Large values of $\beta$ slow down learning, while small values accelerate it.

## Application

Let us now examine the connection between the proposed dynamics and the current algorithms used in the field of machine learning.

In practice, a model is trained by minimizing a loss function $L$, which measures the distance between a model's current state and an expected state. Drawing from classical mechanics, we propose a potential analogous to the gravitational potential:

$$
V = \frac{\beta c^2}{k} L
$$

Where $c^2$ with units of square energy is introduced just to ensure that $L$ remains dimensionless. The choice of this potential is not arbitrary; it is based on the interpretation of the term $\beta/k$ as a thermal mass that amplifies the importance of the distance within the potential energy. Furthermore, we propose a kinetic energy in terms of a mass tensor $M_{ij}$​ of the form:

$$
K = \frac{1}{2} \sum_{i j} M^{ij} Y_{i} Y_{j} = \frac{\beta}{2k}\sum_{ij} g^{ij}X_{i} X_{j} = \frac{\beta}{2k} \mathbf{X}^2
$$

Where $g_{ij}$​ is a dimensionless metric tensor, which we assume for the moment to be constant. In this way, the Hamiltonian is defined as:

$$
H = \frac{\beta}{2k} \mathbf{X}^2 + \frac{\beta c^2}{k} L + E(U, \beta)
$$

Where $E$ is a function of the temperature, enabling us to specify an arbitrary thermal profile. Under this Hamiltonian, the velocity components are given by:

$$
v^{i} = \frac{k}{h\beta} \frac{\partial H}{\partial X_{i}} = \frac{1}{h} X^{i} \qquad  X^{i} = \sum_{ij}g^{ij}X_j
$$

Applying an Euler discretization, the weight update rule can be approximated as:

$$
\mathbf{w}(t) \approx \mathbf{w}(t-\tau) - \frac{\tau}{h} \mathbf{X}(t)
$$

On the other hand, the generalized force driving the learning process has the following components:

$$
F_{i} = -\frac{\beta c^2}{h} \frac{\partial L}{\partial w^{i}} 
$$

By evaluating the components and performing the integration, we arrive at an expression for the impulse as a function of the loss gradient.

$$
\mathbf{I}(t) = -\int_{t-\tau}^t\mathbf{F}(t') dt' = \frac{c^2}{h} \nabla L \int_{t-\tau}^t \beta(t')dt' 
$$

Substituting into the momentum update rule, we obtain:

$$
\mathbf{X}(t) = \frac{\beta(t-\tau)}{\beta(t)}    \mathbf{X}(t-\tau) + \frac{c^2}{h} \left( \frac{1}{\beta(t)} \int_{t-\tau}^t \beta(t') dt'\right ) \nabla L
$$

This tells us that the momenta are updated in terms of time averages of the thermal mass. If we assume a constant temperature, that is, a constant thermal mass:

$$
\beta(t) = \beta
$$

We obtain a constant momentum that depends on the step size:

$$
\mathbf{I}(t) = \frac{\beta c^2}{h} \nabla L \int_{t-\tau}^t dt' =  \frac{\tau c^2}{h}\beta \nabla L
$$

And the update rule will be a historical accumulation of the loss function:

$$
\mathbf{X}(t) = \mathbf{X}(t-\tau) + \frac{\tau c^2}{h} \nabla L
$$

Under a suitable reparameterization, we recover the standard gradient descent or $\text{SGD}$ update rule [@bishop_dl]:

$$
\begin{aligned}
\mathbf{X}(t) = \mathbf{X}(t-\tau) +  \zeta \nabla L
\\
\\
\mathbf{w}(t) \approx \mathbf{w}(t-\tau) - \eta \mathbf{X}(t)
\end{aligned}
$$

Where $\eta$ is the learning rate and $\zeta$ controls the influence of the loss gradient on the momentum.

By adding a harmonic potential to the Hamiltonian such that:

$$
H = \frac{\beta}{2k} \mathbf{X}^2 + \frac{\lambda}{2} \mathbf{w}^2 + V
$$

The generalized force now includes a term consistent with that used in gradient descent with weight decay [@krogh_weight_decay], which proposes adding a term $\lambda \mathbf{w}$ to the loss gradient. This is because an extra term is now added to the force:

$$
F_{\alpha}' = \lambda w_{\alpha}
$$

If we assume that the system cools exponentially, that is, with a thermal mass:

$$
\beta(t) = \beta e^{\gamma t}
$$

We obtain an impulse given by:

$$
\mathbf{I}(t) = \frac{\beta c^2}{h} \nabla L \int_{t-\tau}^t e^{\gamma t'} dt' = \frac{c^2}{h} \frac{1-e^{-\gamma \tau}}{\gamma} \beta e^{\gamma t}
$$

Then, the momentum will be an exponential moving average [@brown_expsmooth] of the loss gradient.

$$
\mathbf{X}(t) = e^{-\gamma \tau} \mathbf{X}(t-\tau) + \frac{1-e^{-\gamma \tau}}{\gamma} \frac{c^2}{h} \nabla L
$$

Again, under a suitable reparameterization, the system reduces to the gradient descent algorithm with momentum and friction [@bottou_sgd]:


$$
\begin{aligned}
\mathbf{X}(t) = \mu \mathbf{X}(t-\tau) + (1-\mu) \zeta \nabla L 
\\
\\
\mathbf{w}(t) = \mathbf{w}(t-\tau) - \eta \mathbf{X}(t)
\end{aligned}
$$

Lastly, we adopt a classical Hamiltonian incorporating relativistic kinetic energy, given by:

$$
H = \sqrt{\mathbf{X}^2 + \frac{k^2}{\beta^2}} + V + E(U, \beta)
$$

This Hamiltonian is a generalization of the previous one, since for small momenta $|\mathbf{X}| \ll k/\beta$, the kinetic energy can be approximated as:

$$
\sqrt{\mathbf{X}^2+\frac{k^2}{\beta^2}} = \frac{k^2}{\beta^2} \sqrt{\frac{\beta^2}{k^2}\mathbf{X}^2 + 1} \approx \frac{k}{\beta} + \frac{\beta}{2k}\mathbf{X}^2 - \frac{\beta^3 (\mathbf{X}^2)^2}{8k^3} + \cdots
$$


The first term, $kT$, corresponds to a rest energy, while higher-order terms are typically discarded. However, recent work on physics-inspired optimizers [@vaidhyanathan_vradam] has shown that retaining higher-order terms in the series can enhance optimization.

Under a relativistic regime, the learning velocity will then be:

$$
v^{i} = \frac{k}{h\beta} \frac{\partial H}{\partial X_{i}} =  \frac{k}{h\beta}  \frac{X^{i}}{ \sqrt{\mathbf{X}^2 + k^2/\beta^2}} = \frac{1}{h} \frac{X^{i}}{\sqrt{\beta^2\mathbf{X}^2/k^2 + 1}}
$$

If we consider $\beta(t) = \beta$ to be constant, we recover the relativistic gradient descent [@franca_conformal], which proposes weight updates of the form:

$$
\mathbf{w}(t) = \mathbf{w}(t-\tau) - \eta \frac{\mathbf{X}}{ \sqrt{\mathbf{X}^2 + k^2/\beta^2}}
$$

However, considering $\beta(t) = \beta e^{\gamma t}$, we observe that $\mathbf{v} \rightarrow 0$ rapidly and the system ceases to learn. This is not an error in the theory; rather, it is due to the fact that we are working under a classical approximation in which the potential is considered decoupled from the metric tensor.

The work of Guskov and Vanchurin on covariant gradient descent [@guskov_covariant] suggests that by embedding the potential into the metric tensor, one recovers adaptive momentum-based optimizers such as $\text{Adam}$ [@kingma_adam] and, as a specific case, the $\text{RMSProp}$ optimizer [@hinton_nn]. Verifying this correspondence explicitly within the current theoretical framework remains as future work.

## Conclusion

The proposed formalism demonstrated that a Hamiltonian framework can recover the majority of current optimization algorithms. This approach moves beyond purely heuristic updates, offering a clear physical interpretation where:

- The loss function acts as a metric distance between system configurations.
	
- Temperature dictates the effective mass, weighting the importance of these distances.
	
- Phase space convergence is guaranteed by the evolution of internal energy.
 
These results lay the groundwork for a new class of physically-informed optimizers. By identifying where current classical approximations fail, such as the decoupling of the potential from the metric tensor, we open new avenues for incorporating covariant and relativistic dynamics into machine learning, potentially leading to more stable and faster convergence in complex loss landscapes.
# Learning Dynamics

The objective of this work is to develop a fundamental theory of the dynamics of artificial learning that not only explains current optimization algorithms, but also enables their improvement and the generation of new ones. To this end, a generic model is proposed, on which three assumptions are made:

- It can be described by a finite number of parameters.

- It is differentiable with respect to its parameters.

- It makes no assumptions about the information it ingests.

The theory is constructed based on the axiomatic thermodynamic framework proposed by Callen [1]. Assuming a quasi-static regime, symplectic geometry is used to describe the geometry of the model’s phase space [5], and a Hamiltonian formalism [6] is employed to derive the model’s equations of evolution.

Finally, these equations are used to re-derive existing algorithms in order to corroborate the theory and to provide a physical interpretation of learning.

### Bibliography

[1] J. C. Baez, “What Is Entropy?”, arXiv:2409.09232, 2024.

[2] J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013.

[3] H. B. Callen, *Thermodynamics and an Introduction to Thermostatistics*, 2nd ed., Wiley, 1985.

[4] V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989.

[5] A. Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics, vol. 1764, Springer, 2001.

[6] H. Goldstein, C. Poole, y J. Safko, *Classical Mechanics*, 3rd ed., Addison-Wesley, 2002.

[7] C. M. Bishop y H. Bishop, *Deep Learning: Foundations and Concepts*, Springer International Publishing, Cham, 2024.

[8] A. Krogh y J. A. Hertz, “A Simple Weight Decay Can Improve Generalization,”
en *Advances in Neural Information Processing Systems*, 1992.

[9] R. G. Brown, *Exponential Smoothing: Forecasting and Control*, Prentice-Hall, 1956.

[10] L. Bottou, “Large-Scale Machine Learning with Stochastic Gradient Descent,”
en *Proceedings of COMPSTAT 2010*, pp. 177–186, 2010.

[11] G. França, J. Sulam, D. P. Robinson, y R. Vidal, “Conformal Symplectic and Relativistic Optimization,” arXiv:1903.04100 [math.OC], 2019.

[12] D. Guskov y V. Vanchurin, “Covariant Gradient Descent,” arXiv:2504.05279 [cs.LG], 2025.

[13] D. P. Kingma y J. Ba, “Adam: A Method for Stochastic Optimization,” arXiv:1412.6980, 2014.

[14] G. Hinton, *Neural Networks for Machine Learning*, Lecture 6e, Coursera (online course), 2012.


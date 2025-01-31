# ReservoirChat_Anonym

Appendix of the project can be found in [Appendix PDF](./appendix.pdf).

ReservoirChat is a specialized AI model **powered by a Large Language Model (LLM)**. It uses a technique called **Retrieval-Augmented Generation (RAG)** to provide *accurate and hallucination-free informations*. It focuses on reservoir computing, and will use the reservoirPy library to code reservoirs. Reservoirs are a pool of randomly connected artificial neurons where, unlike the traditional neuron layers, only the readout layer, which is the last layer, is trained. It thus reduced the effective computational cost.

Unlike traditional LLMs, ReservoirChat integrates retrieval mechanisms and code, related to reservoir computing and the python library [reservoirPy](https://reservoirpy.readthedocs.io/en/latest/). This means it can deliver precise and reliable responses based on external data sources while leveraging large language model's capabilities.

It is important to note that the AI model is **powered by a LLM**, not a reservoir computing neuron network.

The original GraphRAG implementation has been modified to include a streaming functionality based on the method introduced by 6ixGODD : https://github.com/microsoft/graphrag/pull/882
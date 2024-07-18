# Finalizing the project and preparing the presentation

## Presentation

You can find our presentation on [Google Slides](https://docs.google.com/presentation/d/1m0Se6vXWUo9-vSMk6YlZQdPPuVMDCXJme4mlurWnxHI/edit?usp=sharing).

## Weekly Progress Report

### Backend Challenges and Solutions

#### What's new

1. **Separated General Users:** We have separated general users who participate in the allocation process into a separate domain entity called "Participant". Users can be a part of one or more specific allocations. This allows us to improve the user experience by allowing users to reuse their existing account for multiple allocations.
2. **New GraphQL API:** We have implemented a GraphQL API with create, read, update, and delete operations for all domain entities: allocations, form fields, participants, their preferences, rooms, and users.
3. **Collected Requirements:** We have collected new requirements and made changes to our domain entities based on these requirements.
4. **GraphQL Node Resolver:** We have implemented GraphQL Node Resolvers with lazy loading and caching for all entities and their relationships.

#### Challenges

Our main challenge was implementing a GraphQL API, as our team had main experience with REST APIs. The challenges we faced were:
1. Permissions and control access management. This part is a weak point of GraphQL APIs since access control policies are content-dependent and not separatable as in REST APIs.
2. Performance issues. In comparison to REST APIs, we can not cache whole requests and their responses due to dynamic nature of GraphQL APIs.
3. Circular references in GraphQL Node definitions.

#### Solutions

However, with effort of the team members, we solved all these challenges with production ready solutions.
1. Permissions and control access management is done with permission resolvers wich operate with custom user roles and contexts, allowing very flexible access control policies.
2. Performance issues are solved with lazy loading and caching fetched objects in dataloaders. Using dataloaders, allows us to cache every independent object and invalidate cache very easily on object changes.
3. Circular references were solved using lazy types. Lazy types are types that are not resolved until they are needed, so we can resolve references in runtime from a common type pool.

#### Next Steps

There is still a lot of work to do, but we are close to finishing the project. Next steps would be:
1. Finilizing business logic of the application.
2. Integration with Telegram Bot and ML models.
3. Improving access control policies and ensuring security.

### ML Challenges and Solutions
1. **NLP**. We have started the realization of a system that would allow us to compare full-text answers of users.
For that we use word embeddings, dimensionality reduction (PPA-PCA) and an ensemble of BM25 and FAISS.
2. **Successful alternative experiments**. Our ML team never stops experimenting. This time we have composed a sufficient metric Hybrid metric with random forest, as well as a couple other minor experiments.
3. **Integration of ML into backend**. We started the integration of ML models into the backend environment. This process has yet to take one more week, since both the backend and ML implementations are of considerable size and dependencies. 

#### Conclusions and Next steps
This week we saw a significant progress in enhancing user experience through NLP and ML.  We partially developed a system for comparing full-text user answers using word embeddings, dimensionality reduction, and a hybrid approach of BM25 and FAISS.  Our ML team experimented with a new Hybrid metric using random forest, showing their commitment to continuous improvement.  Integration of ML models into the backend is underway, with anticipated completion within a week.  This integration will significantly improve the platform's functionality and user experience. 

Our future focus includes completing the full-text answer comparison system and ensuring seamless ML integration into the backend. As well as debug our entire system to prepare for the accommodation of new students and couple week later. These efforts will deliver a more robust, efficient, and personalized platform for our users.

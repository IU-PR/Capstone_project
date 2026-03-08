![repo-banner](https://github.com/user-attachments/assets/42104349-189b-40d8-b7ba-5b102e72ba98)

> Tier: Personal  
> Customer: Undisclosed  
> Repo: https://github.com/IU-Capstone-Project-2025/hypershelf  

# Feedback

TL;DR: customer is impressed, but asked for some additional features

> [!NOTE]
> From the last week:
> - ACL to limit access to assets
> - Full REST API with access tokens
> - Discuss existing solution for office schema generation with \[REDACTED\]
> - Store cold history of all changes made with link to dates, users and ability to rollback
> - Add ability to group by fields

New feedback after multiple customer demos this week:
- Multiple events
- Query builder
- Enforce Markdown field format

# Iteration

## Implemented features based on user feedback

See **Weekly progress** section

## Performance & Stability

Since the app uses self-hosted Convex, it is intended to be used in small teams (<300 people), otherwise it becomes harder to manage and poses some stability risks. Convex itself handles such pressure fine, but it becomes a severe infra management overhead with large amount of users on a self-hosted instance.


## Documentation

Everything is self-explanatory

# Weekly progress

## Query builder 🆕

![CleanShot 2025-07-09 at 1  46 48@2x](https://github.com/user-attachments/assets/fb1b1eca-f149-40fb-9d75-ec18b2e72e5c)

Allows to construct any filtering query based on the asset data. Supports wide range of operators and is very flexible in terms of future work - query can be exported as SQL string or any other popular filtering type, including JSON Logic, which is used for on-client filtering.
Due to its power, closes many issues at once:
- Multiple events
- Query builder
- Add ability to group by fields

## Refactoring

- Consistent return types of similar methods for different structures (fields, assets, views, users).
- Consistent naming conventions for API methods
- Separate API for lock logic

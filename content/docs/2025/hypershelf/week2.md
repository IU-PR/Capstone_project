
![repo-banner](https://github.com/user-attachments/assets/42104349-189b-40d8-b7ba-5b102e72ba98)

> Tier: Personal  
> Customer: Undisclosed  
> Repo: https://github.com/IU-Capstone-Project-2025/hypershelf  


# Detailed Requirements

All of the requirements were specified in the Week 1 report and are sufficient on the current stage.

# Prioritized Backlog

Since I am working following the waterfall development model **and** working alone, I do not really need a specific backlog. Currently the next priorities (in the random order) are:
- Office schemas & vSphere integration
- Deep vSphere integration on the backend
- Markdown editor
- Static views for users (which columns in which order)
- Bug fixes
- UX/UI improvements

# Project Progress

## Detect errors in the table

All errors, as well as empty required fields are now highlighted

<img width="469" alt="Screenshot 2025-06-18 at 2 32 28 PM" src="https://github.com/user-attachments/assets/ef4035fc-7319-4879-95d3-19548d9a4a8a" />

## UX/UI improvements

<img width="1206" alt="Screenshot 2025-06-18 at 2 33 35 PM" src="https://github.com/user-attachments/assets/ec6d5a13-0739-4ca7-8f3a-c8bb08a7ae31" />


## More field types

All field types have validators specific to them. E.g. `IP Address` type has validator `subnet`, which is the CIDR notation subnet.

<img width="1206" alt="Screenshot 2025-06-18 at 2 36 31 PM" src="https://github.com/user-attachments/assets/b04ac616-4eb4-43fd-a315-d4d9660293cc" />


## Client-side vSphere integration

Links the Hypershelf widget to the asset using hostname (in this case portal.dev.\[REDACTED\]).
I also want it to show the position on the office schema in the widget (plans for future)

![Pasted image 20250618143905](https://github.com/user-attachments/assets/0f44bc33-af9c-4eae-8744-6c648c940a52)

## Debug Interface

Available for all fields, one specific field, all assets and one specific asset. Useful in plugin development to see the fields available on each field, and, obviously, for debug.

<img width="1206" alt="Screenshot 2025-06-18 at 2 41 51 PM" src="https://github.com/user-attachments/assets/158dc7ca-5b0b-4dd4-adff-a7eef3ef4d69" />

## Persistent Fields

Prevents the deletion of a specific field. Useful for plugin development to prevent ID changes. Though it is not recommended to address fields by ID, it is still possible.

<img width="1206" alt="Screenshot 2025-06-18 at 2 43 01 PM" src="https://github.com/user-attachments/assets/c6ccfe42-498a-4d78-8a09-2c860225a744" />

## Bug fixes

Most of the bugs were fixed as the result of codebase refactor.

## DX Best Practices

Codebase for frontend was very much refactored to follow best practices of React & follow DRY.

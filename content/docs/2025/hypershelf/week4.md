![repo-banner](https://github.com/user-attachments/assets/42104349-189b-40d8-b7ba-5b102e72ba98)

> Tier: Personal  
> Customer: Undisclosed  
> Repo: https://github.com/IU-Capstone-Project-2025/hypershelf  

# Testing and QA

This week's patch includes **integration tests** for Convex backend with 100% test coverage.
The testing pipeline tests isolated components, as well as their interaction between each other.

<img width="529" alt="Screenshot 2025-07-01 at 3 40 45 PM" src="https://github.com/user-attachments/assets/ec0dd6cc-65d7-458d-b09e-d99e47f309c2" />

<img width="822" alt="Screenshot 2025-07-01 at 3 42 10 PM" src="https://github.com/user-attachments/assets/95ff9e3f-cf38-4e23-9a2e-69e9589b4b75" />

Frontend E2E tests would require spinning up a separate Convex server with a full configuration, which is pretty tough. As of now, there is only a plan for E2E tests:
1. Spin up a compose inside a worker
2. Import a pre-built Convex backup mock into a temporary server
3. Run E2E tests using Playwright

# CI/CD

Current CI/CD setup includes a GitHub workflow

1. Run integration tests in a worker
2. Create GitHub deployment
3. Push changes to the server using SSH and re-build the compose

In plans for future:
1. E2E tests
2. Smoke test with rollback in case of production failure

<img width="856" alt="Screenshot 2025-07-01 at 3 48 09 PM" src="https://github.com/user-attachments/assets/eaa29de7-85de-477f-bf75-5e4a7eb88ad0" />

# Deployment

Initial setup is manual, no CI/CD. If the target server does not have an already deployed version of Hypershelf, the pipeline will fail.

1. Run `docker compose up -d`. This will spin up the containers.
2. Run `docker compose exec -ti backend ./generate_admin_key.sh` to get `CONVEX_SELF_HOSTED_ADMIN_KEY`.
3. Log in to Convex dashboard.
4. Set up Convex environment:

<img width="747" alt="Screenshot 2025-07-01 at 3 55 10 PM" src="https://github.com/user-attachments/assets/02bec820-8982-4859-82f9-474d862156e8" />

5. Run `bunx convex deploy`.
6. Set up environment variables (guide in `.env.sample`):

<img width="683" alt="image" src="https://github.com/user-attachments/assets/c8f04fa0-412b-4404-a35c-b98f27aa2fc5" />

7. Run `docker compose restart`.
8. Set up nginx/openresty using `hypershelf.app.conf`. Openresty is recommended, nginx might need to be built with lua in order to support `proxy_cookie_flags`.
9. Set up your domains `convex.example.com`, `backend.example.com`, `convex-dashboard.example.com`, `example.com`. In case of Cloudflare you can use wildcard:

<img width="1050" alt="image" src="https://github.com/user-attachments/assets/6829f74a-f88d-4818-abf6-63c5badb7d5f" />

10. Enjoy

Any consequent changes to this instance will be deployed through CI/CD automatically if you set up the secrets inside GitHub repo:
- `DEPLOYMENT_URL`: public URL of deployed frontend, e.g. `https://hypershelf.app`. Will be used as deployment url.
- `SSH_HOST`: IP of the target server
- `SSH_PRIVATE_KEY`: OpenSSH private key with access to deploy
- `SSH_USER`: Either `root`, or user with `NOPASSWD` permissions for Docker + `/opt/hypershelf`

# Vibe Check

All of my teammates feel heard, trust me on this one. Progress is steady and on-schedule. We've had a demo for the customer and got some valuable feedback + requested features

<img width="333" alt="image" src="https://github.com/user-attachments/assets/3d92bffd-afbe-4d77-9f9b-314766a8caf9" />

- ACL to limit access to assets
- Full REST API with access tokens
- Discuss existing solution for office schema generation with \[REDACTED\]
- Store cold history of all changes made with link to dates, users and ability to rollback
- Add ability to group by fields

# Weekly progress
## Static views

Allows to hide and reorder columns, as well as set the sorting rules. The views are stored on the backend, the currently preferred view is stored client-side.

<img width="1207" alt="Screenshot 2025-07-01 at 4 15 00 PM" src="https://github.com/user-attachments/assets/1f000ee1-0a8d-482d-ba5a-9b298774a221" />

<img width="1207" alt="Screenshot 2025-07-01 at 4 16 10 PM" src="https://github.com/user-attachments/assets/87842245-453e-42e1-9265-a78f61f3e85b" />

<img width="1207" alt="Screenshot 2025-07-01 at 4 17 24 PM" src="https://github.com/user-attachments/assets/841b4461-c0ae-45e4-a360-6b13b13f7b02" />

## Integration tests

<img width="783" alt="Screenshot 2025-07-01 at 4 18 19 PM" src="https://github.com/user-attachments/assets/cfe84c2e-86c4-4a7f-81d5-ab8400880c7b" />

## CI/CD

<img width="437" alt="Screenshot 2025-07-01 at 4 19 24 PM" src="https://github.com/user-attachments/assets/f493935c-2591-47bd-88fc-3fb29cf6d2ae" />

## Better UI

Sizing, margins, glass-morphic elements

<img width="456" alt="Screenshot 2025-07-01 at 4 21 16 PM" src="https://github.com/user-attachments/assets/bd0642c2-d186-4aff-ae44-e07e84b334e6" />

## Better UX

Improved state management, better accessibility.

## Bug fixes

Fixed list elements validation, fixed minor logical bugs.

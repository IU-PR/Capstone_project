![repo-banner](https://github.com/user-attachments/assets/42104349-189b-40d8-b7ba-5b102e72ba98)

> Tier: Personal  
> Customer: Undisclosed  
> Repo: https://github.com/IU-Capstone-Project-2025/hypershelf  

# Links

- **Deployment**: [hypershelf.app](https://hypershelf.app)
- **Repo**: [hypershelf](https://github.com/IU-Capstone-Project-2025/hypershelf)
- **Presentation**: [hypershelf.pdf](https://drive.google.com/file/d/1XSutzNivMjXNc6rCxgh8ERMbynBsObhY/view?usp=sharing)
- **Legal notice**: [legal.pdf](https://drive.google.com/file/d/1h8I2rYOIqH1Tai-Ey69zWterW8kGEyi8/view?usp=sharing)

# Final deliverables

## Project overview

There is a real problem in digital assets management. Most of the existing systems are non-reliable, expensive, do not follow Russian laws, or hard to use. Hypershelf aims to solve all of these problems.

## Features

- Live sync
- Mutex
- Query builder
- Static views
- Markdown editor
- Integrations

## Tech stack
- Next.JS
- PostgreSQL
- Convex
- Docker
- Openresty

## Setup instructions

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

## Presentation draft

See **Links**

## Weekly commitments

- Daniil Gazizullin: See **Links**

## Plan for Next Week

- Refine the presentation
- Refine the project in terms of the legal field


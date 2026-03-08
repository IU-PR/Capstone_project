
![repo-banner](https://github.com/user-attachments/assets/42104349-189b-40d8-b7ba-5b102e72ba98)

> Tier: Personal  
> Customer: Undisclosed  
> Repo: https://github.com/IU-Capstone-Project-2025/hypershelf  

# MVP Features

- Auth
- Field editing
- Asset editing
- Mutex locks
- vSphere plugin
- Production-grade UI/UX

# Week 3 results

## Markdown editor

The editor was tailored to mimic one of Obsidian. Obsidian uses *HyperMD*, which is the wrapper around CodeMirror 5. Hypershelf uses bare CodeMirror 6 with a lot of custom extensions and blocks. It is based on https://github.com/segphault/codemirror-rich-markdoc with significant changes.
- Blockquotes
- Lists (ordered, unordered, tasks (WIP))
- Tables (WIP)
- Links
- Files
- Images
- Formatting: *italic*, **bold**, ~~strike~~, highlight
- Callouts: info, warning, error
- Headings
- Code: blocks and inline

<img width="882" alt="Screenshot 2025-06-25 at 1 19 15 PM" src="https://github.com/user-attachments/assets/8cd9ffb2-8e74-4007-9544-84da1247e334" />
<img width="882" alt="Screenshot 2025-06-25 at 1 19 30 PM" src="https://github.com/user-attachments/assets/d5f5034f-2ba9-4730-b4ee-2191e7f9fd1f" />
<img width="882" alt="Screenshot 2025-06-25 at 1 19 39 PM" src="https://github.com/user-attachments/assets/4414888d-c24d-42c6-b1ad-ec5fefad41af" />

## Architecture

Due to the lack of time and resources, as well as the computing power to deploy multi-instance HA architecture, I decided to bail on it in favor of single-instance. Now the project can be deployed using Docker compose. Though, as mentioned earlier, it is still pretty hard.
The project is deployed at https://hypershelf.app and is accessible for testing (ask for Invite Code).

![image](https://github.com/user-attachments/assets/bb2a035a-8d61-4004-a44c-985390c274ef)

The repo structure was completely changed, see the latest commit for more details.

## Authentication

It was a tough decision. The best option for MVP is to patch all cookies to be `SameSite=None, Secure` and integrate [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API) to request user's permission to access those cookies inside iframes. It is a bald security choice, but good enough for an MVP. The only better way I see is to completely rewrite Convex client authentication layer and request authentication tokens using plugin through `window.postMessage`.
Because of the limitations of the Storage Access API, it is now required to click the iframe before it can load any data:

<img width="547" alt="Screenshot 2025-06-25 at 1 33 41 PM" src="https://github.com/user-attachments/assets/eaaa3eaf-7d36-4b65-be54-8fd0457d4040" />

## UI

Significant fixes for UI glitches, better UI on assets management page, footer with useful information, plugin installation guide, and much more

<img width="1209" alt="Screenshot 2025-06-25 at 1 35 17 PM" src="https://github.com/user-attachments/assets/6390c2f5-8218-4f9c-bcb1-6f382679e60d" />
<img width="508" alt="Screenshot 2025-06-25 at 1 35 34 PM" src="https://github.com/user-attachments/assets/ef04ff57-0c23-4c9c-a2d4-f6635e20e3e2" />

The plugin is now built and packed during build time to be ready-to-serve.

## Client-side validation

It was present on Week 2, but now it is much more robust. Applies to asset management view (read-only) and to asset editing form. Next week - the same for fields.

<img width="1081" alt="Screenshot 2025-06-25 at 1 38 07 PM" src="https://github.com/user-attachments/assets/515c596c-41d7-4f5b-8a8c-e87658abc1db" />

## Adaptive UI

Since it's a universal system, it should be fully accessible on any device.

<img width="1504" alt="Screenshot 2025-06-25 at 1 40 19 PM" src="https://github.com/user-attachments/assets/d9e7ba54-670a-4f85-a592-18bb18d87aab" />
<img width="1504" alt="Screenshot 2025-06-25 at 1 41 10 PM" src="https://github.com/user-attachments/assets/6859a23e-3ae3-40ff-a688-999a3e5be59d" />
<img width="1504" alt="Screenshot 2025-06-25 at 1 42 18 PM" src="https://github.com/user-attachments/assets/df87e7a9-bc3d-4480-a964-a22c11538862" />

## Licensing

Proper adherence to the GNU AGPL v3 guidelines.

# Plans

The MVP will very soon be shown to the potential customer for demo, so currently most of the plans include tailoring and bugfixes.
Next up:
1. Fields validation
2. Static views
3. Office schemas + vSphere integration
4. Maybe PWA
5. Maybe `draw.io` / Excalidraw inside Markdown
6. More

# Weekly commitments

- Daniil Gazizullin: [f924a16](https://github.com/IU-Capstone-Project-2025/hypershelf/commit/f924a1634aad1b549a6e00700cb867da31608721)

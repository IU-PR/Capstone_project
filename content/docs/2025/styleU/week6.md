# Week #6

### Deployment: **[styleU](http://94.228.169.104:5173)**
### Design: **[figma](https://www.figma.com/design/VHOnHId7DlFbgjnn46NGUW/StyleU?node-id=264-642&p=f&t=rrd38MvDvcf5fUPw-0)**

## 1. Final deliverables

### Project overview
Our project is an AI stylist that helps a person choose looks for events and returns a set of things with links where they can be ordered, while it takes into account the cost of goods, as well as the features of a person's figure and color type - therefore, it chooses not just trendy goods, but also what will suit a person personally

### Features

- color type definition by photo + personal recommendations from AI

- body type definition by parameters + clothing recommendations

- image selection for an event based on the user's personal request - all you have to do is follow the link and order


### Tech stack

- ML: numpy, PIL, skimage, sklearn, cv2, mediapipe, torch, clip

- Backend: python, mongo, posgres, fastAPI

- Frontend: Jsx(vite)+react+TailwindCSS

### Setup instructions

1. clone repo
2. create **.env** file by example - we can send you all passwords
3. run **docker-compose up**

or

1. go to our [deployed version](http://94.228.169.104:5173) & try it 



## 2. Presentation draft

We have only plan for presentation:

- Slide about marketplace statistics + popularity of rice with clothing reviews => decided to study this topic
- Slide about the target audience
- Slide about the fact that many people, as it turned out, have problems with choosing clothes (here show graphs from our survey) and highlight a list of reasons
    - Clothes are expensive
    -    <….>
    - They don’t know their color type

- Here it’s worth telling in more detail about the color type - we provide a diagram where the difference in color types is visible + a link to an article and a video from YouTube2 slide show what color types look like (cut photos from Pinterest)
- Conclusion from all this - we decided to make an AI stylist who will determine the body type, color type and recommend images made up of real products from popular marketplaces with the ability to see how these things will look on a person

- Here you can slide about the team and about the fact that they worked on an agile type
 ____________________________________________
- Slide about feature 1 color type - an example of how it works, why it is useful for the user, they can think about buying clothes in colors that suit them or just compare that things in these shades will suit them less
    - Slide about ML - how this thing works in general with an example of a graph
- Slide about feature 2 figure - an example of how it works and why it is useful - like we tell about the features of the figure, throw in ideas about what suits and what doesn't + then we use this feature to select images, also tell here in 1-2 sentences how it works

- Slide about feature 3 image selection
    - An example of how it works from the user's side, like entered data received an image
    - Explanation of what lies behind it - a diagram + tell about the parser
- Slide about the avatar feature - clarify that the idea came from a trend on Instagram (this is close to our target audience) and then it may develop into a 3D model, for now it's just a picture to see how things go together and send to a friend??

Now about how it all works inside
- Alena will talk about the general architecture of the product and delve into the back- Alena will also talk about the database and authorization
- Aisylu will tell what model we use and how it all works
- Katya and Masha will talk about the front and design
    - How we chose the design, about the survey, etc.
    - About the architecture of the front and what we used for writing, you can talk about the translation here

- Life demonstration

## 2. Individual contribution of each participant

1) Ksenia Korchagina (lead) - organize work, write report, make presentation



2) Yasmina Mamadalieva - fix problems with parser and some frontend issues

https://github.com/IU-Capstone-Project-2025/styleU/commit/ad5cb8f13159240e86dfb6fd00fc7f588b2b8bad

https://github.com/IU-Capstone-Project-2025/styleU/commit/599bccd69590a3255405bf893c46fe624429920a

https://github.com/IU-Capstone-Project-2025/styleU/commit/c7dd3c66dfe3ea39c1ddb5dbe9f827c7c43d4e8e




3) Aisylu Fattakhova - fix llm issues and connect it to backend

https://github.com/IU-Capstone-Project-2025/styleU/commit/6f89116324ff1f08892f0eba5870da9c826c8335

https://github.com/IU-Capstone-Project-2025/styleU/commit/893b4a708a0e602678ef4f1ba785d77a30eff617

https://github.com/IU-Capstone-Project-2025/styleU/commit/ba5d56b6feb7e6949a5fd5b329603218b59e0985

https://github.com/IU-Capstone-Project-2025/styleU/commit/f3311e9135a3ad27339fbf7b18a0673e591f49da



4) Ekaterina Akimenko - make 3 feature frontend & connect it to back

https://github.com/IU-Capstone-Project-2025/styleU/commit/f0c03f73639d0d3250bae55a36ca4a28497801c9

https://github.com/IU-Capstone-Project-2025/styleU/commit/fdd94de3690d5f003e1497fbade8bf893edc4723

https://github.com/IU-Capstone-Project-2025/styleU/commit/fb6202b154429549dfe1dedc91cdd597fcb86d3e

https://github.com/IU-Capstone-Project-2025/styleU/commit/df5e386e7c04d87584cfed4ebb661accab1fede7

https://github.com/IU-Capstone-Project-2025/styleU/commit/830951340f1d531a43c25e9ed71e4c0c95784d60

https://github.com/IU-Capstone-Project-2025/styleU/commit/fb6202b154429549dfe1dedc91cdd597fcb86d3e


5) Sofia Goryunova - trained the model for the color type

https://github.com/IU-Capstone-Project-2025/styleU/commit/0221e1627451d675bdfb651806a5b4ca05ad752b


6) Alena Starikova - connect back with parser, help girls to connect everything

https://github.com/IU-Capstone-Project-2025/styleU/commit/845ee391018db7d243f3245dafa674a5a658115e

https://github.com/IU-Capstone-Project-2025/styleU/commit/6f89116324ff1f08892f0eba5870da9c826c8335

https://github.com/IU-Capstone-Project-2025/styleU/commit/893b4a708a0e602678ef4f1ba785d77a30eff617

https://github.com/IU-Capstone-Project-2025/styleU/commit/79ae27c677085c0ac4f46a9d094c60b2ee8cfcef

https://github.com/IU-Capstone-Project-2025/styleU/commit/9d2f71fc167e950a833f938f6c88b642d1a01086

https://github.com/IU-Capstone-Project-2025/styleU/commit/845ee391018db7d243f3245dafa674a5a658115e

7) Rokkel Maria - write personal page in frontend


https://github.com/IU-Capstone-Project-2025/styleU/commit/c6e1bc1038ed5b2e7cf9701c5fa36805fc68a674

https://github.com/IU-Capstone-Project-2025/styleU/commit/9b63a1d7e1f26ff221590b4ea7f5db402989c235


## 3. Plan for Next Week

- Create presentation
- Interract with users & get feedback
- Make Demo presentation
- Fix all bugs
- Test our service
- Finilize last feature

[Link to kanban board](https://s5-project-summer-2025.teamly.ru/space/45e22f1e-f31f-4207-96f3-dd8a18b314b8/database/f226fd43-ad24-45a2-ac21-8f5c7684f4c6)

---
title: "Week #4"
---

# **Week #4**

## Testing and QA

### Automated Testing of the Back End

### Manual Testing of the Android Application

- **Testing Method:** manual testing was conducted without documented checklists
  or test cases, as QA worked independently.
- **Reasoning:** manual testing was chosen to save time since only one
  regression test is planned (at the end of the course) and the app’s design is
  rapidly evolving, making UI test automation inefficient.
- **Results:** four bugs were identified
  ([bug report 1](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=116973603&issue=evops-sum25%7Cevops-android%7C22),
  [bug report 2](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=117538274&issue=evops-sum25%7Cevops-android%7C28),
  [bug report 3](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=118202715&issue=evops-sum25%7Cevops-android%7C30),
  [bug report 4](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=118203273&issue=evops-sum25%7Cevops-android%7C31))
- **Mobile Specific Features Tested:**
  - The application retains state after screen rotation and theme changes.
  - A network disconnection does not terminate the app.

### Evidence of Test Execution

[https://github.com/evops-sum25/evops/actions/runs/16034532112/job/45243008806](https://github.com/evops-sum25/evops/actions/runs/16034532112/job/45243008806)

## CI/CD

**CI:**

Our CI/CD is configured via
[GitHub Actions.](https://github.com/features/actions) All configuration files
are placed in the [main repository](https://github.com/evops-sum25/evops). There
are three CI files for the three major submodules of our project. Here are their
workflows:

**Back End / ML Server:**

1. Install the stable Rust toolchain and Protobuf compiler.
2. Run `cargo check` to check if the code can build.
3. Run `cargo test` to execute unit, integration, and documentation tests.
4. Run `cargo fmt --all --check` to check whether the code is formatted.
5. Run `cargo clippy -all-targets` to catch common lints.

**Website:**

1. Set up Node.js and pnpm.
2. Get the pnpm store path and cache the dependencies.
3. Run `pnpm install` to install dependencies.
4. Run `pnpm lint` to catch common lints.
5. Run `pnpm test` to test the code.
6. Run `pnpm typecheck` to check type safety.

**CD:**

Our Continuous Deployment is configured in a single file. Its workflow should be
triggered manually in the GitHub UI because of the `on: workflow_dispatch`
setting in the CD configuration file. Here is the workflow:

1. Install `sshpass` to run SSH using the keyboard-interactive password
   authentication mode, but in a non-interactive way.
2. Connect to our server using the secret variables we’ve set in the repository
   settings.
3. Fetch updates and update submodules.
4. Rebuild and rerun the Docker containers.

### Links to CI/CD Configuration Files

- [Website CI file](https://github.com/evops-sum25/evops/blob/main/.github/workflows/website-ci.yaml).
- [Back end CI file](https://github.com/evops-sum25/evops/blob/main/.github/workflows/backend-ci.yaml).
- [ML server CI file](https://github.com/evops-sum25/evops/blob/main/.github/workflows/ml-server-ci.yaml).
- [CD file](https://github.com/evops-sum25/evops/blob/main/.github/workflows/single-server-cd.yaml).

## Deployment

### Staging

A prototype instance of our application is hosted on a server that we bought on
[HostVDS](https://hostvds.com/). For the Continuous Deployment file, we’ve set
these environment variables in our repository:

- `SERVER_USER`: Unix username.
- `SSH_PASSWORD`: Unix password.
- `PROJECT_PATH`: filesystem path to the project.
- `SEVER_HOST`: IP address of the server.

As was mentioned in the CI/CD part, we trigger the deployment workflow manually.
It helps us avoid unnecessary rebuilds and gives us more control over our
deployment.

### Production

Due to the self-hosted nature of our project, we are not supposed to have a
single production instance. For the purposes of the Capstone Project course, you
can think of our staging deployment (described above) as the production
instance. However, the plan has always been to allow users to host their own
EvOps in-house.

## Vibe Check

The vibe check was successfully conducted during the last team meeting, where we
enjoyed delicious barbecue. 😋

Team health check results: _very positive vibe_. 😎💯

There has been good progress overall, and no major obstacles have been
identified. Some members indicated that they might require assistance with their
designated task. Consequently, team members will be offering each other support.

Team dynamics remain healthy, with open communication and effective
collaboration. All members have participated actively and felt comfortable
sharing.

## Weekly Commitments

### Individual Contribution of Each Participant

#### Aleksandr Isupov

- Created styles
  ([commit 1](https://github.com/evops-sum25/evops-android/commit/21cdc956a25220c228f4f518cd9f304f6c697851),
  [commit 2](https://github.com/evops-sum25/evops-android/commit/435f3260fb8e516151a2047e085ff861dd6b628d)):
  - Added and integrated typography text styles.
  - Fitted images into squares with a blurry background on the Event List
    screen.
  - Refactored element positioning on the Event List and Event Details screens.
  - Added animated transitions to navigation.
  - Added loaders to network images.
- Tested the application manually and found several bugs
  ([bug report 1](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=116973603&issue=evops-sum25%7Cevops-android%7C22),
  [bug report 2](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=117538274&issue=evops-sum25%7Cevops-android%7C28),
  [bug report 3](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=118202715&issue=evops-sum25%7Cevops-android%7C30),
  [bug report 4](https://github.com/orgs/evops-sum25/projects/1/views/1?pane=issue&itemId=118203273&issue=evops-sum25%7Cevops-android%7C31)).
- Fixed bugs found during manual testing:
  - Navigation bar icons did not show the selected screen
    ([commit](https://github.com/evops-sum25/evops-android/commit/6d1ded434efaea0a63f1fd8c068ccbaeac9a3f66)).
  - When navigating via the navigation bar, the stack of screens was not cleared
    ([commit](https://github.com/evops-sum25/evops-android/commit/a6006a000e9cd58fd2dd6e0d864faf5c2465ea7c)).
  - The top app bar on the Event Details screen had double status bar paddings
    ([commit](https://github.com/evops-sum25/evops-android/commit/21cdc956a25220c228f4f518cd9f304f6c697851#diff-759ebb9ff4e55c0d9af6b8947131e2f1b198d965545df11ffb5f233566aeb6c8)).
  - The navigation bar did not return to the Event List screen when clicking the
    Home icon on the Event Details screen
    ([commit](https://github.com/evops-sum25/evops-android/commit/d94340e8e9eed1c5f253edf8aa55bc8191d8cb50)).
- Refactored the code written quickly before the MVP
  ([commit 1](https://github.com/evops-sum25/evops-android/commit/6beb41cf08a1c8df5d1dca5d1c7686b176c03cd8),
  [commit 2](https://github.com/evops-sum25/evops-android/commit/6b7121f1053ec3d1307e739ea23b1b6e64eee986)).

#### Arsen Galiev

- Added i18n support to the website
  ([commit](https://github.com/evops-sum25/evops-website/commit/6c5bffd7b2c213d04fbd7da27b7115d6d13cf2ac)).
- Updated the UI of the event creation page
  ([commit](https://github.com/evops-sum25/evops-website/commit/6c5bffd7b2c213d04fbd7da27b7115d6d13cf2ac)).
- Fixed ESLint issues
  ([commit](https://github.com/evops-sum25/evops-website/commit/7a51884d954d061fe6b41bb793882dd2ad7de8dc)).

#### Asqar Arslanov

- Connected the back end to MinIO
  ([commit](https://github.com/evops-sum25/evops-backend/commit/d0e12348fad02d528d33b94b0b49099ca36314f8)).
- Covered the Markdown parser and validation logic with tests
  ([commit](https://github.com/evops-sum25/evops-client-ext/commit/2faea6bbf87e08f4869f1fd782583a1c8230deef)).
- Introduced major changes to the back end codebase
  ([PR](https://github.com/evops-sum25/evops-backend/pull/39)):
  - Added support for image uploads through API endpoints.
  - Decoupled domain models and API schemas better.
  - Organized the code communicating with the database.

#### Egor Pustovoytenko

- Refactored back-end database communication
  ([PR 1](https://github.com/evops-sum25/evops-backend/pull/38),
  [PR 2](https://github.com/evops-sum25/evops-server-ext/pull/1)).
  - Moved `evops-db` to `server-ext` for usage by the ML server.
  - Refactored the architecture of modules in the back end.
- Connected ML to the back end
  ([directory](https://github.com/evops-sum25/evops-ml/tree/main/server)).
- Fixed small bugs
  ([commit](https://github.com/evops-sum25/evops-ml/commit/be8e1a9f4fb6cfe4421ba78a17eedc2d5094e929)).

#### Ilya-Linh Nguen

- Wrote all web CI/CD workflow
  ([commit 1](https://github.com/evops-sum25/evops/commit/e729030fb7768b4e37cbb9df56a6fd82d14337a9),
  [commit 2](https://github.com/evops-sum25/evops/commit/0c50701509e7b51c681fe683407c1ff341b62d4c),
  [commit 3](https://github.com/evops-sum25/evops/commit/aec654b13f072dce9024af6cb360eb46e94ebb76),
  [commit 4](https://github.com/evops-sum25/evops/commit/b9793b5d29e222188615a30c9d6e48df7c0f64b4),
  [commit 5](https://github.com/evops-sum25/evops/commit/0d3f8021346f3b082fed17e2fb97cb1475b2bad5)).
- Added MinIO storage for images in Docker Compose
  ([commit](https://github.com/evops-sum25/evops/commit/443be480ae15d4e1efb83dc07dd44f96807780e5)).
- Published a new Android release
  ([release](https://github.com/evops-sum25/evops/releases/tag/v0.3.0)).

#### Maksim Ilin

- Replaced the previously found dataset (Yambda) with the MovieLens
  [dataset](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset)
  because of better fitting.
- Augment the MovieLens dataset with the movie descriptions and perform
  embeddings creation and dimensionality reduction
  ([commit](https://github.com/evops-sum25/evops-ml/commit/21e04568129d66d957939a48c943346d74747464)).
- Extracted persons with the highest amount (99.99 percentile) of reviews (20M
  to 78,000 rating entries) and created a user’s profile builder function
  ([commit](https://github.com/evops-sum25/evops-ml/commit/244acee1947afcd665e83bcd1f4efbb5de7769d0)).

#### Ramil Shakirzyanov

- Evaluated the recommendation system on the MovieLens dataset
  ([commit](https://github.com/evops-sum25/evops-ml/commit/5f7d51ec06397d2505e3662a1618d8830517e72a)).

## Plan for Next Week

### DevOps

- Fix errors with the dev and HMR Dockerfiles.
- Buy a domain for the website.
- Make a CI/CD pipeline for the Android application.

### Machine Learning

- Discuss the idea of machine text translation of posts.
- Implement the template for the recommendation system service class.

### Back End

- Add more endpoints.
- Preprocess incoming images.
- Continue working on issues from previous weeks.

### Android

- Update Create Event screen to include new fields: tags, location, date & time
  (depends on the back end).
- Integrate new fields to the Event Details screen (depends on the back end).
- Make the search field on the Event List screen functional (depends on the back
  end).
- Add validation to the Event List screen form.
- Add image posting.
- Add loaders to all the network dependent screens.

### Website

- Integrate Connect Query and solve caching issue in [Next.js](http://Next.js).
- Add support for new features from our back end.
- Improve the UI in existing pages.

## Confirmation of the Code’s Operability

We confirm that the code in the `main` branch:

- [x] Is in working condition.
- [x] Runs via Docker Compose.

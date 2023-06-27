# Telegram Commands

## Start

> `/start` -> starting point of using bot

Bot will ask time when it is allowed to set a task

Format:

> [**start_time**]-[**end_time**]

Could be either in 24h format or 12h format

Example:

> `13:00-2:00`

or 

> `11:00AM-2:00PM`


## Task and/or events manipulation

---

### Addition of events or tasks

##### Tasks

> `/add_task` -> adds task according to info in specific format or according to questionnaire

Specific format could be:

> [**task_name**]-[**duration** (in minutes)]-[**importance**]-[**complexity**]-[start_time]-[date]

(start_time and date are optional)

Example

> `Sport-90-3-1-9:00-1/1/1970`

##### Events

> `/add_event` -> adds event according to info in specific format or according to questionnaire

Specific format could be:

> [**event_name**]-[**start_time**]-[**duration** (in minutes)]-[Number] [day | {day of week (e.g. Sunday)} | month] [Number of events]

Where last arguments are provided using space between them.
Last argument is for repeated events. [Number] is a number of second argument to pass to repeat event. [Number of events] is the number of repetitions of the event.  
(for example, 2 Sunday 3 - repeat every second sunday three times)

Last argument is optional

Example

> `AML-11:00-90-2 Sunday 3`



### Changing tasks or events (Edit)

##### Tasks

> `/edit_task` -> edits task according to info provided by user

There should be list of tasks to choose (implemented as buttons attached to message) for editing 

After choosing task there should be list of available info that could be changed in the task.

##### Events

> `/edit_event` -> edits event according to info provided by user

There should be list of events to choose (implemented as buttons attached to message) for editing

After choosing event there should be list of available info that could be changed in the event.

### Deletion of tasks or events

##### Tasks

> `/delete_task` -> deletes task that user chose from list of tasks

List should be implemented as buttons attached to message

##### Events

> `/delete_event` -> deletes event that user chose from list of events

List should be implemented as buttons attached to message

### List

> `/list {[today, tomorrow, week] or specific date or telegram date input}` -> shows events and tasks for specified date

List should be implemented as buttons attached to message

Specific date format:

> `dd/mm/yyyy`

Example:

> `1/1/1970`

### Plan

> `/plan` -> creates timetable for the next day considering events for the next day and list it in message or as buttons attached to message. Should be request to export suggested timetable

---

## Mark history

---

### Start task

> `/start_task` -> saves time of starting task

There should be list of tasks attached to message

### End task

> `/end_task` -> saves time that user spent on task

There should be list of **active** tasks attached to message

### History manipulation

> `/add_task_history` -> sends users report for specific completed task (chosen by user)

User should the following info:
- real complexity of task
- whether the task was completed
- time of start and end of the task (optional)

List should be implemented as buttons attached to message

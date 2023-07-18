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

> [**task_name**]-[**duration** (in minutes)]-[**importance**]-[start_time]-[date]

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

### List

> `/list {[today, tomorrow, week] or specific date or telegram date input}` -> shows events and tasks for specified date

List should be implemented as buttons attached to message

Specific date format:

> `dd/mm/yyyy`

Example:

> `1/1/1970`

### Plan

> `/plan` -> creates timetable for the next day considering events for the next day and list it in message.

---

## Mark history

> `/add_task_history` -> sends users report for specific completed task (chosen by user)

User should the following info:
- whether the task was completed
- time of start and end of the task (optional)


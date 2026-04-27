
---

# Etapa 8 — atualizar teu ficheiro de notas com o que já sabemos
No `docs/project_notes.md`, substitui pelo seguinte:

```markdown
# Applied Databases Project Notes

## Core marking requirements
- Implement all required menu options
- Use MySQL and Neo4j correctly
- Ensure project runs from main.py
- Keep regular GitHub commits over time
- Add GitLink.txt in root
- Add innovation document in root
- Ensure compatibility with VM

## Menu options
1. View Speakers & Sessions
2. View Attendees by Company
3. Add New Attendee
4. View Connected Attendees
5. Add Attendee Connection
6. View Rooms
x. Exit application

## Confirmed details from spec so far

### Option 1 - View Speakers & Sessions
- Ask user for a full or partial speaker name
- Show:
  - speaker name
  - session title
  - room name
- If no match, show no speakers found message

### Option 2 - View Attendees by Company
- Ask for company ID
- A valid company ID is any number greater than 0
- Keep prompting until a valid company ID is entered
- If company does not exist, show:
  - Company with ID X doesn't exist
- If company exists but has no attendees in sessions, show:
  - No attendees found for [CompanyName]
- Otherwise show attendee-related details

### Option 3 - Add New Attendee
- Ask for:
  - attendee ID
  - name
  - DOB
  - gender
  - company ID
- On success show:
  - Attendee successfully added
- Error cases:
  - attendee ID already exists
  - invalid gender
  - company ID does not exist
  - database-reported input errors may be shown

### Option 4 - View Connected Attendees
- Ask for attendee ID
- Show attendee name
- Show all attendees connected via CONNECTED_TO in either direction
- If attendee exists in MySQL but not Neo4j:
  - show attendee name
  - show No connections
- If attendee exists in neither DB:
  - show attendee does not exist error

## Still to confirm
- Option 5 exact rules
- Option 6 exact rules
- Exact formatting for final outputs
- Any additional constraints for Neo4j insertion
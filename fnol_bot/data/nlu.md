## intent:greet
- Hi
- Hey
- Hi bot
- hi
- hello

## intent:affirm
- yeah
- correct
- ye

## intent:request_faq
- im looking for answers to my questions
- looking for details.
- have concerns.
- looking for details

## intent:inform
- my policy number is [POL3321096489](policy)
- the policy number is [POL3321096477](policy)
- policy number is [POL3321096343](policy)
- my policy number is [POL3121096489](policy)
- the policy number is [POL3221096477](policy)
- policy number is [POL3321226343](policy)
- my policy number is [POL1222096489](policy)
- the policy number is [POL1231096477](policy)
- policy number is [POL3321123343](policy)
- my policy number is [POL1121096489](policy)
- the policy number is [POL1212096477](policy)
- policy number is [POL1111096343](policy)
- my last name is [Smith](last_name)
- the last name is [Deshmukh](last_name)
- last name is [Kamble](last_name)
- my last name is [raju](last_name)
- the last name is [route](last_name)
- last name is [sahit](last_name)
- my last name is [robert](last_name)
- the last name is [zennon](last_name)
- last name is [tiger](last_name)
- my unique id number is [15476239](unique_id)
- the unique id number is [15476333](unique_id)
- unique id number is [15476222](unique_id)
- my unique id number is [15122529](unique_id)
- the unique id number is [16676533](unique_id)
- unique id number is [15476677](unique_id)
- my unique id number is [15476999](unique_id)
- the unique id number is [15473213](unique_id)
- unique id number is [15476990](unique_id)
- my date of birth is [22/03/1996](dob)
- the date of birth is [20/06/1996](dob)
- date of birth is [22/07/1996](dob)
- my date of birth is [11/03/1996](dob)
- the date of birth is [20/11/1996](dob)
- date of birth is [22/12/1996](dob)
- my date of birth is [31/03/1996](dob)
- the date of birth is [30/06/1996](dob)
- date of birth is [22/06/1996](dob)
- zipcode is [99503](zip_code)
- my zipcode is [99510](zip_code)
- the zipcode is [99521](zip_code)
- zipcode is [99512](zip_code)
- my zipcode is [99511](zip_code)
- the zipcode is [99331](zip_code)
- zipcode is [92303](zip_code)
- my zipcode is [11510](zip_code)
- the zipcode is [49521](zip_code)
- my policy number is [POL1234567899](policy)

## intent:chitchat
- can you share your boss with me?
- i want to get to know your owner
- i want to know the company which designed you
- i want to know the company which generated you
- i want to know the company which invented you
- i want to know who invented you
- May I ask who invented you?
- please tell me the company who created you
- please tell me who created you
- tell me more about your creators
- tell me more about your founders
- Ahoy matey how are you?
- are you alright
- are you having a good day
- Are you ok?
- are you okay
- Do you feel good?
- how are things going
- how are things with you?
- How are things?
- how are you
- how are you doing
- how are you doing this morning
- how are you feeling
- how are you today
- How are you?
- How is the weather today?
- What's the weather like?
- How is the weather?
- What is the weather at your place?
- Do you have good weather?
- Is it raining?
- What's it like out there?
- Is it hot or cold?
- Beautiful day, isn't it?
- What's the weather forecast?
- Is it quite breezy outside?

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:thankyou
- thanks
- thankyou

## intent:goodbye_intent
- bye
- goodbye
- see you around

## regex: dob
- [0-31]/[0-12]/[0-9]{4}

## regex: policy
- [POL][0-9]{13}

## regex: unique_id
- [0-9]{8}

## regex: zip_code
- [0-9]{5}

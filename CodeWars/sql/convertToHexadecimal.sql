/*
to hexYou have access to a table of monsters as follows:

monsters table schema
id
name
legs
arms
characteristics
Your task is to turn the numeric columns (arms, legs) into equivalent hexadecimal values.

output table schema
legs
arms
*/
select to_hex(arms) as arms, to_hex(legs) as legs from monsters
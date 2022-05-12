{switch(s1;s2;s3)}.

bulb(off) :- not bulb(on).
bulb(on) :- switch(s1), switch(s3).
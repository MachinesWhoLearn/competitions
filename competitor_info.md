# Competition Info
Spring quarter 2016 we will be competing in Kaggle competitions. We will likely cover some information from the following resources at our first meeting of the quarter.

## Kaggle

To compete on the MachinesWhoLearn Kaggle team for a given competition, you must either be invited (if the team already exists), or create the team yourself. To do either of these things requires you to sign up for a personal Kaggle account.

[Kaggle FAQ](https://www.kaggle.com/wiki/KaggleMemberFAQ)

[Team Information](https://www.kaggle.com/wiki/FormingATeam)

For more general questions, refer to the [Kaggle Wiki](https://www.kaggle.com/wiki/Home).

## AWS

If you would like to train your model on a more powerful machine than your personal computer, let an MWL officer know (or sign up for an IAM account at the first meeting).

Amazon has given us $200 in AWS credits to use, but they expire on January 31, 2017 so use them up!

To give some context, $200 gets you:
* 400 hours on a m4.2xlarge instance (8 cores, 32 GB of ram)
* 300 hours on a g2.2xlarge instance (8 cores, 15 GB of ram, 1 GPU)

Assuming you're paying on-demand pricing for a Linux machine.

But, if you're feeling economical, you may use spot pricing - which will get you 1000 and 1200 hours on the same machines, respectively.

Don't worry too much about expenses, though. If we have 10 club members using AWS, and each club member needs a g2.2xlarge instance for 1 hour each week of the school year (including summer quarter!) to train their awesome deep learning model, then we'll use less than 10 * 30 * $0.6 = $180 by the time 1/31/17 rolls around.

### How to use AWS as an IAM user

1. If you don't yet have an IAM account through MWL, email a MWL officer with your preferred username and some sort of identification that you go to UW and/or have attended MWL meetings in the past.
2. We will email you back with your username and a temporary password.
3. Go to https://483727235907.signin.aws.amazon.com/console and login.
4. Set a new password when prompted.
5. Click on EC2 in your AWS management console (it's the only AWS service you have access to).

After that, it's up to you what to do. Launch an instance or manage your existing instances.

You will have control over ALL of MWL's EC2 resources. With great power comes great responsibility. Don't terminate anyone else's instances or "borrow" someone else's storage volume. There is one exception: If you see that someone's instance has been running for more than 24 hours, you have permission to *stop* it. In all likelihood, someone forgot to stop or terminate their instance after they were done using it, and now they're just wasting everyone's money. This leads us to the \#1 rule of EC2.

### The \#1 Rule of EC2

DON'T FORGET TO STOP OR TERMINATE YOUR INSTANCE AFTER YOU ARE DONE USING IT.

Amazon charges by the hour, so a g2.2xlarge instance forgotten for a day will cost 24 * $0.6 = $14.40 and one forgotten for a week or two will just about deplete all our money for the year. I typically use instances for 1-2 hours at a time, and expect the same typical usage pattern from others. Things that you can do offline, such as writing code, should be done before you start up an instance. If you're ever in doubt about how to use EC2 or AWS, let us know! 

If this talk about wasting all the club's money scares you, don't worry! AWS has a free tier, that allows us to rent t2.micro instances for free, up to 750 hours a month. These instances only have 2 cores and 1 GB of ram, so they're not much help for training big models, but they're great for learning.

## Conclusion

 AWS may be daunting at first, but you don't have to use it to build great models! Kaggle typically only has 2-3 competitions a year that require massive amounts of computing power. The rest may be taken on with the typical quad-core laptop or PC. And if you're just getting started with machine learning it's not likely you'll need even that much power for a while.

Good luck, and happy model building!

\- Phil

%%%
    Title = "RFC Evaluation Project: First Step"
    abbrev = "RFC-Eval"
    category = "experimental"
    docName= "draft-huitema-rfc-eval-project"
    ipr = "trust200902"
    area = "Network"
    date = 2019
    [pi]
    toc = "yes"
    compact = "yes"
    symrefs = "yes"
    sortrefs = "yes"
    subcompact = "no"
    [[author]]
    initials="C."
    surname="Huitema"
    fullname="Christian Huitema"
    organization = "Private Octopus Inc."
      [author.address]
      email = "huitema@huitema.net"
      [author.address.postal]
      city = "Friday Harbor"
      code = "WA  98250"
      country = "U.S.A"
%%%

.# Abstract
This document presents a first attempt at evaluating the production of the IETF.
We analyze a set of randomly chosen RFC approved in 2018, looking for history
and delays, and using Google Scholar as a proxy for the RFC popularity. The
results are interesting, and inform further evaluation efforts.
{mainmatter}

# RFC Evaluation project

As stated on the organization's web site, "The IETF is a large open international
community of network designers, operators, vendors, and researchers concerned with
the evolution of the Internet architecture and the smooth operation of the Internet."
In this memo, we start exploring how the IETF could possibly be evaluated, and we
do so by attempting to evaluate the RFC production process.

The IETF data tracker provides information about RFC and drafts, from which we can
infer statistics about the production system. We can measure how
long it takes to drive a proposition from initial draft to final publication,
and how these delays can be split between Working Group discussions, IETF reviews,
IESG assessment, RFC Editor delays and final reviews by the authors.

Just measuring production delays may be misleading. The IETF
produces standard proposals and informative memos that get published in the RFC
series, but that is not its only purpose. Two other purposes would be the
organization of fruitful discussions between members of the technical community,
and the filtering of ill-thought proposals so they are not endorsed in
IETF publications.

To try assess this other purposes, we have to find ways to measure the impact
of the documents that were published. If the communication between participants
was efficient, the documents should be easily accepted by the community. If bad
ideas were filtered, the specifications should lead to deployed product and
services with good feedback.

A potential failure mode of the IETF is to do too much filtering. After all,
classifying a proposal as ill-thought or potentially harmful is subjective.
A comprehensive analysis would look at the fate of proposals that were not
accepted by the IETF but got developed in other ways and became eventually
successful. We will not try to assess that in this memo, but further
studies migh consider the issue.

# Methodology

In this exploration, we want to evaluate not just the mechanics of the RFC
production, but also the quality and impact of the results. This evaluation of
quality and impact is subjective. We start with two ideas:

1- Use Google Scholar to assess the citation counts of published documents

2- Ask the RFC authors whether the specifications resulted in the
   deployment of products or services

Basic production mechanisms could be evaluated by processing data from
the IETF tracker, but subjective data requires manual assessment of results,
which can be time consuming. Since our resources are limited, we will only
perform this analysis for a small sample of RFC, selected at random
from the list of RFC approved in 2018. Specifically, we will pick
10 RFC at random between:

* RFC 8307, published in January 2018, and

* RFC 8511, published December 2018.

In order to avoid injecting personal bias in the random selecton, we use
a random selection process similar to the Nomination Committee selection
process defined in {{!RFC3797}}. The process is seeded with the text string
"vanitas vanitatum et omnia vanitas", and the results are:
~~~ 
Picking 10 numbers between 8307 and 8511,
using MD5(vanitas vanitatum et omnia vanitas)
Rank 1: 8411 -- md5=daba041224a879199b698748808f917d
Rank 2: 8456 -- md5=f5570484d91ada6a672edbdca61d808c
Rank 3: 8446 -- md5=8340e918bb8faf69d197f79c9a58d7b8
Rank 4: 8355 -- md5=19474df74efd9917cf3fe8acce2ac374
Rank 5: 8441 -- md5=5acce2b730f3c24a4a91a5fc1921d1cd
Rank 6: 8324 -- md5=411c11a1cf4c292f83458865599c6921
Rank 7: 8377 -- md5=ac16a89192c0f0727febd35aacbc1f24
Rank 8: 8498 -- md5=bba44f2ba1ab240a1265a82ab71f7e02
Rank 9: 8479 -- md5=1653606b0af95d529a473a8f85ffaea4
Rank 10: 8453 -- md5=0cbfe105667c5a83b027dcfa85062f98
~~~


# Analysis of each RFC

We review each of the RFC listed in {{#methodology}}, trying both to answer the known
questions and to gather insight for further analyzes.

## RFC 8411
IANA Registration for the Cryptographic Algorithm Object Identifier Range {{!RFC8411}}:
~~~
Informational, 5 pages
4 drafts (personal),first May 8, 2017. Published August 2018.
Last call announced 2017/10/09
IESG evaluation starts 2017/12/28
Approved 2018/02/26, draft 03
Auth 48 2018/04/20
Auth 48 complete 2018/07/17
Published 2018/08/06
IANA action: create table
~~~
The draft underwent minor copy edit before publication. 

The long delay in Auth48 is probaby due to clustering with {{!RFC8410}}, which entered
AUTH 48 on 06/05. The MISSREF tracker code was cleared then.

There is no reference for this RFC on Google Scholar.

## RFC 8456
Benchmarking Methodology for Software-Defined Networking (SDN) 
Controller Performance {{!RFC8456}}.
~~~
Informational
64 pages
2 personal drafts, 9 WG drafts, first in March 2015
Last call announced 2018-01-19
IESG evaluation starts 2018-02-27
IESG approved 2018-05-25
Auth 48 2018-08-31
Auth 48 complete 2018-10-16
Published 2018-10-30
~~~
The draft underwent very extensive copy editing, covering use of articles, turn of phrases, choice
of vocabulary. The changes are enough to cause pagination differences. The “diff” tool marks pretty
much every page as changed. Some diagrams see change in protocol elements like message names.

The RFC was part of cluster with {{!RFC8455}}.

Google Scholar shows 2 citations.

## RFC 8446
The Transport Layer Security (TLS) Protocol Version 1.3 {{!RFC8446}}
~~~
Proposed standard
160 pages
29 WG drafts first April 17, 2014.
Last call announced 2018/02/15
IESG evaluation starts 2018/03/02
Approved 2018/03/21, draft 28
Auth 48 2018/06/14
Auth 48 complete 2018/08/10
Published 2018/08/10
~~~
Copy editing includes explaining acronyms on first use, clarifying some definitions 
standardizing punctiation and capitalization, and spelling out some numbers in text.
This generally fall in the category of “style”, although some of the clarifications
go into message definitions.

122 citations in Google Scholar.

## RFC 8355
Resiliency Use Cases in Source Packet Routing in Networking (SPRING) Networks {{!rfc8355}}
~~~
Informational, 13 pages.
2 personal drafts (personal), first January 31, 2014. 13 WG drafts.
Last call announced 2017-04-20
IESG evaluation starts 2017-05-04, draft 09
Approved 2017-12-19, draft 12
Auth 48 2018-03-12
Auth 48 complete 2018-03-27
Published 2018-03-28
~~~
Minor set of copy edit, mostly for style.

It appears that publication waited for availability of RFC 8354. There is no formal dependency
between the two RFC, but they appear to have been clustered.

7 references on Google Scholar.

## RFC 8441
Bootstrapping WebSockets with HTTP/2 {{!rfc8441}}
~~~
Proposed standard, 8 pages. Updates RFC 6455.
3 personal drafts (personal), first 10/15/2017. 8 WG drafts.
Last call announced 2018-05-07, draft 05
IESG evaluation starts 2018-05-29, draft 06
Approved 2018-06-07, draft 07
Auth 48 2018-08-13
Auth 48 complete 2018-09-15
Published 2018-09-21
IANA – table entries
~~~
Minor set of copy edit, mostly for style.

No references on Google Scholar. (RFC 6455 had 1000 results)

## RFC 8324
DNS Privacy, Authorization, Special Uses, Encoding, Characters, Matching, and Root Structure:
Time for Another Look? {{!rfc8324}}
~~~
Informational, 29 pages. Independent stream.
5 personal drafts (personal), first June 2, 2017.
ISE review started 2017-07-10, draft 03
IETF conflict review and IESG review started 2017-10-29 
Approved 2017-12-18, draft 04
Auth 48 2018-01-29, draft 05
Auth 48 complete 2018-02-26
Published 2018-02-27
~~~
Minor copy edit, mostly for style. One whole paragraph added in conclusion.

1 reference on Google Scholar.

## RFC 8377
Transparent Interconnection of Lots of Links (TRILL): Multi-Topology {{!rfc8377}}
~~~
Proposed standard, 20 pages. Updates RFC 6325, 7177.
3 personal drafts (personal), first September 3, 2013. 7 WG drafts.
Last call announced 2018-02-19, draft 05
IESG evaluation starts 2018-03-02, draft 06
Approved 2018-03-12, draft 05
Auth 48 2018-04-20, draft 06
Auth 48 complete 2018-07-31
Published 2018-07-31
IANA Table, table entries
~~~
Minor set of copy edit, mostly for style, also clarity.

No references on Google Scholar.

[[TODO: Ask authors why it took so long to get the draft adopted by the WG]]

## RFC 8498
A P-Served-User Header Field Parameter for an Originating Call Diversion (CDIV)
Session Case in the Session Initiation Protocol (SIP) {{!rfc8498}}.
~~~
Informational, 15 pages.
5 personal drafts (personal), first March 21, 2016. 9 WG drafts.
Last call announced 2018-10-12, draft 05
IESG evaluation starts 2018-11-28, draft 07
Approved 2018-12-10, draft 08
Auth 48 2019-01-28
Auth 48 complete 2019-02-13
Published 2019-02-15
IANA Action, table rows added.
~~~
Copy edit for style, but also clarification of ambiguous sentences.

No references on Google Scholar.

## RFC 8479
Storing Validation Parameters in PKCS#8 {{!rfc8479}}
~~~
Informational, 8 pages. Independent stream.
5 personal drafts (personal), first August 8, 2017.
ISE review started 2018-03-29, draft 02
IETF conflict review and IESG review started 2018-03-29
Approved 2018-08-20, draft 03
Auth 48 2018-09-20, draft 04
Auth 48 complete 2018-09-25
Published 2018-09-26
~~~
Very minor set of copy edit, moving some references from normative to informative.

No reference on Google Scholar.

## RFC 8453
Framework for Abstraction and Control of TE Networks (ACTN) {{!rfc8453}}
~~~
Informational, 42 pages.
3 personal drafts, first June 15, 2015. 16 WG drafts. Published Aug 2018.
Out of WG 2018-01-26, draft 11
Expert review requested, 2018-02-13
Last call announced 2018-04-16, draft 13
IESG evaluation starts 2018-05-16, draft 14
Approved 2018-06-01, draft 15
Auth 48 2018-08-13
Auth 48 complete 2018-08-20
Published 2018-08-20
IANA Action, table rows added.
~~~
Minor copy editing.

7 references on Google Scholar.

# Initial observations

[[TODO: Update as we refine the analysis and get deployment data.]]

The initial list of results shows the distribution of delays
between the various stages of the process:

RFC | Status | Pages | Overall | WG | IETF | IESG | RFC ED | Auth48 | RFC Pub
---! | !---  | ----! | -----! | --! | ---! | ---! | -----! | -----! | ------!
8411 | Info | 5 | 455 | 154 | 80 | 60 | 53 | 88 | 20
8456 | Info | 64 | 1107 | 823 | 39 | 87 | 98 | 46 | 14
8446 | Standard | 160 | 1576 | 1400 | 15 | 19 | 85 | 57 | 0
8355 | Info | 13 | 1517 | 1175 | 14 | 229 | 83 | 15 | 1
8441 | Standard | 8 | 341 | 204 | 22 | 9 | 67 | 33 | 6
8324 | ISE | 29 | 270 | 38 | 111 | 50 | 42 | 28 | 1
8377 | Standard | 8 | 1792 | 1630 | 11 | 10 | 39 | 102 | 0
8498 | Info | 15 | 1061 | 935 | 47 | 12 | 49 | 16 | 2
8479 | ISE | 8 | 414 | 233 | 0 | 144 | 31 | 5 | 1
8453 | Info | 42 | 1162 | 1036 | 30 | 16 | 73 | 7 | 0
Average |  | 35.2 | 969.5 | 762.8 | 36.9 | 63.6 | 62 | 39.7 | 4.5

The average delay from first draft to publication is about 2.5 years, but this
varies widely. The average document is discussed for 2 years in the working
group, undergoing many revisions.
The extreme case is {{!RFC8377}}. It took 2 years for the WG to adopt the draft,
and then another 2.5 years before the WG submitted the document for publication.
The next longest case is {{!RFC8446}}, the definition of TLS 1.3. The WG spent
lots of time discussing and validating the specification, conducting
interoperability tests and studying deployments.

The time spent in the AUTH48 state varies widely. In theory, this is just a final
verification: the authors receive the document prepared by the RFC production center,
and in theory just have to give their approval, or maybe request a last minute
correction. The name indicates that this is expected to last just two days, but
in average it lasts more than a month. [[TODO: ask authors of RFC 8411, 8456, 8446
and 8377 why the AUTH48 phase took so long.]]

Out of 10 randomly selected RFC, 2 were published through the "independent series".
One is an independent opinion, the other a description of a non-IETF protocol
format. The publication delays were significantly shorter than for IETF stream RFC.
This seems to indicate that the Independent Series is functioning as 
expected. The authors of these 2 RFC are regular IETF contributors, but we would
need to analyse more than 2 samples to draw conclusions.

Part of the exercise is to test whether citation counts provide a useful
measure of the popularity of the IETF production. These citation counts
vary widely:

RFC | Status | Scholar
---! | !---- | -----!
8411 | Info | 0
8456 | Info | 2
8446 | Standard | 122
8355 | Info | 7
8441 | Standard | 0
8324 | ISE | 1
8377 | Standard | 0
8498 | Info | 0
8479 | ISE | 0
8453 | Info | 7

The results indicate that {{!RFC8446}} is by far the most popular of the 10
RFC in our sample. This is not surprising, since TLS is a key Internet Protocol.
We need however to be a bit cautious before asserting that publications with
a low citation count have limited impact:

* some documents may well accumulate more citations over time. For example,
  {{!RFC8377}} updates {{!RFC6455}}. There are more than 1000 citations of
  {{!RFC6455}} on Google Scholar. We might expect that the citation count
  of {{!RFC8377}} will increase in the coming years.

* citation counts largely come from academic publications, and thus reflect
  popularity within researchers more than popularity with network operators
  and vendors.

We should be able to assess the popularity of specifications with vendors,
operators and designers by asking questions about deployed services and products.

# Next steps

The current version of this draft is very much a preliminary exercise. It
suffers from at least two limitations:

* The sample size of 10 is certainly too small

* We have yet to obtain responses from authors about deployments, and also
  explanantion of delays.

We need to fix these two points in the next edition of the draft.

Even with those limitations, the exercise shows some promise, and also
shows the interest of doing more studies. For example, one of the plausible
questions is whether the IETF impact is increasing or decreasing over time.
We could do that by repeating the statistical sampling analysis for previous
years, for example 2008 and 1998.

# Security considerations

This draft does not specify any protocol.

We might want to analyze whether security issues were discovered after
publication of specific standards.

# IANA Considerations

This draft does not require any IANA action.

Peliminary analysis does not indicate that IANA is causing any particular
delay in the publication process.

# Acknowledgements

TBD

{backmatter}











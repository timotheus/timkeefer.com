
===Day 1 Keynotes===

http://www.choosealicense.com - github license

NuPIC Open-Source project 
    - Nuro science - http://numenta.org

Open Compute Project

SocialCoding4Good

clj-drone - open project to control a done using closure
    - gigasquid on github
 
inBloom (github) - school k-12 solutions
    - needs help
    - hack for oppertunity idea

Ubuntu - phone & tablet announcement
    - QML SDK
    - More computing & better battery life  
    - HTML5 Toolkit
    - Supports Android apps 
    - Juju - jujucharms.com - now on macosX
    
VIM - w/ Damian
    - color col match
    - next marker
    - list listchars
      set listchars to display unwanted tabs and extra spaces
    - noremap ; :
    - autoswap_mac 
    - mkspell (highlight unwanted words)
    - vmath.vim
    - vis.vim
    - dragvisuals.vim
    - thoughtstream/Damian-Conway-vim-script on github

Twisted + Selenium
    - Run Twisted as the proxy, which can cache all assests
    - can be used to help test tracking
    - http://www.youtube.com/watch?feature=player_embedded&v=HKNZ-tQQnSY
    - webpagetest.org

Phonegap: The Good, The Bad
    - http://goo.gl/qrPqe1
    - browserscope.org
    - no web workers in the webview
    - js operations will block
    - dooes not support for gingerbread for inability to do sub-element scrolling
    - don't do software scrolling
    - disable pinch zoom
    - turn off format detection (phone, address, etc)
    - use native spinner window.navagion...
    
    Phonegap APIs
    - geolocation is tuff -- stale points
    - .getLastKnowPosition()
    - JS Maps in webview - way too slow, don't do it
    - events apis: debounce pause/resume
    - use winere
    - push logging to a server, helps debug startup failures

Using Python on Hadoop
    - mrjob (yelp's wrapper around map reduce)
    - my take away is there's no good support for hadoop in python

Software Design
    - http://www.oscon.com/oscon2013/public/schedule/detail/29205
    - n00b, Second system effect, too clever by half, realism, Nirvana

Keynotes Thursday
    - Code2040 - non-profit
    - hack for diversity
    - "The Stark Principle"
    - MIT - no restrictions, no liabilty
    - GPLv2 - too many restrictions
    - whitehouse.gov "We The People" open-source, open data -- online petitions
      whitehouse death star petition
      http://www.whitehouse.gov/developers
      
Docker - @solomonstre
    - https://github.com/dotcloud/docker
    - virtualbox w/ docker installed
      docker ps
      docker build git://github.com/steeve/docker-opencv
      docker run [image name]
    - image index: index.docker.io

Data collection in health care research
    - Project Harvest 
    - pip install harvest
    - ModelTree
      Avacado: db model field abstraction
    - Serrano: RESTful APIs
    - Cilantro:
    - can be applied to any complex data model, e.g. non-profits, e-commerce
      github.com/cbmi

The Internet of Things
    - The 3 laws of robots by Issac Assimov

Hacking w/ Your Kids - 5 Tips
  Slides: http://www.slideshare.net/nearyd/growing-next-generation

    1) creative toys - must be fun
       Kaplas (wooden blocks)
       Idea train sets
       Meccano (errector sets) http://www.meccano.com/
    
    2) Hackable living space
       Build, paint your home stuff w/ them

    3) Grow a garden w/ them

    4) Arts and crafts
       - leave things laying around (fabric, art stuff, paper, glue guns)
       - homemade costumes
       - toothpicks, corks and paper rolls
       - egg float experiment (salt water)
   
    5) teach electronics
        - take apart toys, flashlights and put them into something else
          solar panel & motors

    6) Coding literacy
        Scratch App, KHAN Academy

    ** Sharing is good (e.g. participate in group experiments)
       freedom is not having to ask permission

    ** Allow kids to control their enviroments

    ** 5 monkeys experiments - lever and food and shower


Closing Keynotes:
    - distinction: borrow it from someone else :) e.g. "Graduated from MIT"

Cryptography Pitfalls (@jtdowney)
    AES, RSA, DES
    - https://speakerdeck.com/jtdowney/cryptography-pitfalls-at-oscon-2013
    - NIST goverment standards
    - DES (modified by gov -- backdoor?)
    - GPG for stored data encryption
    - Use high level libs in languages Keyczar
    - Use OpenSSL random
    - Hash functions or finger prints
      use sha-256 over MD5
      use HMAC-SHA-256 for signatures
      don't use ECB, use CBC cyper block chaining
      Use AES
      enable verity peer in ebaysdk
      https://www.coursera.org/course/crypto
      http://pragmaticcrypto.com

SocialCoding4Good
    - HFOSS Hunanitarian Open-source
    - Mifos (mico-finance open-source project)
    - Prep Instructions for participants
      1) have a corp github account
      2) know how to create a repo, commit, etc
      3) things to bring
      4) if existing apps, then build instructions are needed

Javascript MVC
    - http://www.mozart.io/
    - headless browsers to fix seo issues
    - degradation sucks, duplication work
    - Bigcommerce (shopping cart service)
      overlay wizard
      mobile app using PhoneGap
      todomvc.com
      http://www.unrealengine.com/html5/
    
Other
  - Devops Book
    http://itrevolution.com/books/phoenix-project-devops-book/

  - Bash Programming
    http://cdn.oreillystatic.com/en/assets/1/event/95/BASH%20as%20a%20Modern%20Programming%20Language%20Presentation%201.ppt
    
  - 3D Tree.js: http://www.oscon.com/oscon2013/public/schedule/detail/28557
  - http://talks.golang.org/2013/bestpractices.slide
  - http://cdn.oreillystatic.com/en/assets/1/event/95/New%20Rules%20For%20JavaScript%20Presentation.pdf
  - http://cdn.oreillystatic.com/en/assets/1/event/95/The%20good,%20the%20bad,%20and%20how%20to%20avoid%20the%20Ugly%20-%20PhoneGap%20on%20Android%20Presentation.pdf
  - http://cdn.oreillystatic.com/en/assets/1/event/95/Was%20It%20Something%20I%20Said_%20The%20Art%20of%20Giving%20_and%20getting_%20Actionable%20Critiques%20Presentation.pdf

Feature: Index Page

Just some simple sanity checks on the index page of the application
This also serves as a good test that the lettuce and selenium
stuff is all hooked up properly and running.

    Scenario: Index Page Load
        Given I am not logged in
        When I access the url "/run/new/"
        Then I see the page title "capsim: "

    Scenario: Index Page Load With Selenium
        Using selenium
        When I access the url "/run/new/"
        Then I see the page title "capsim: "
        Finished using selenium

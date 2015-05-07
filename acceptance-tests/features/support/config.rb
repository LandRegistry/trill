require 'capybara/cucumber'
require 'capybara/poltergeist'
require 'selenium-webdriver'

include Capybara::DSL

Capybara.default_selector = :xpath
Capybara.default_driver = :poltergeist
Capybara.javascript_driver = :poltergeist
Capybara.default_wait_time = 10
Capybara.app_host = 'http://localhost:4567' # change url

Capybara.register_driver :poltergeist do |app|
 Capybara::Poltergeist::Driver.new(app, :inspector => true)
 # line below added to stop cucumber/ruby re-raising javascript errors (dog 7/5/15)
 Capybara::Poltergeist::Driver.new(app, {js_errors: false})
end
### Includes the unit testing framework
require 'test/unit'
### Allows the functions (assert_equals to work)
include Test::Unit::Assertions

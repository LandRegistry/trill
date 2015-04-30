After do | scenario |
  # If the scenario failed let's take a screenshot. It helps for debugging
  if (scenario.failed?)
      save_screenshot("sshot-#{Time.new.to_i}.png", :full => true)
  end
end

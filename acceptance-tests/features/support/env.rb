
#
# You shouldn't use like http://fixtures.landregistry.local as this will work locally
# but not in CI. So we need to use variables which can be over written.
# The commands below work as:
#   $URL_Variable_Name = (If_Not_Empty_Then_Use_This_Value ||(OR) This_Is_The_Default_Value )
#
# The ENV[] are defined as system variables.
#

$TRILL_APPLICATION_URL = (ENV['TRILL_APPLICATION_URL'] || 'http://localhost:5000/signin')

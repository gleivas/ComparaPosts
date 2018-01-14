Feature: comparar posts

  Scenario: verificar se ha o mesmo post no blog e no twitter
     Given um post
      When verificamos se ele esta no twitter
      And verificamos se ele esta no blog
      Then o teste passara se estiver nos dois


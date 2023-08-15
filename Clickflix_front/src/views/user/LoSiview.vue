<template>
  <div class="section userinfo_profile-all">
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center py-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
          <h6 class="mb-0 pb-3 h6class">
            <span>Log In </span>
            <span>Sign Up</span>
          </h6>
          <input class="checkbox" type="checkbox" id="reg-log" name="reg-log">
          <label for="reg-log"></label>
            <div class="card-3d-wrap mx-auto">
              <div class="card-3d-wrapper">
                <div class="card-front">
                  <div class="center-wrap">
                    <div class="section text-center">
                    <h4 class="mb-4 pb-3 h4class">Log In</h4>
                      <form @submit.prevent="logIn">
                        <div class="form-group">
                          <input type="email" name="username" class="form-style" placeholder="Your Email" id="username" v-model="username" autocomplete="off">
                          <i class="input-icon uil uil-at"></i>
                        </div>
                        <div class="form-group mt-2">
                          <input type="password" name="password" class="form-style" placeholder="Your Password" id="password" v-model="password" autocomplete="off">
                          <i class="input-icon uil uil-lock-alt"></i>
                        </div>
                        <input type="submit" class="aclass logbtn mt-4" value="logIn">
                      </form>
                      <p class="mb-0 mt-4 text-center pclass"><a href="#0" class="aclass link">Forgot your password? (나중에할수있으면 하기)</a></p>
                    </div>
                  </div>
                </div>
                <div class="card-back">
                  <div class="center-wrap">
                    <div class="section text-center">
                    <h4 class="mb-4 pb-3 h4class">Sign Up</h4>
                    <form @submit.prevent="signUp">
                      <div class="form-group">
                        <input type="text" name="nickname" class="form-style" placeholder="Your NickName" id="nickname" v-model="nickname" autocomplete="off">
                        <i class="input-icon uil uil-user"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input type="email" name="signusername" class="form-style" placeholder="Your Email" id="signusername" v-model="signusername" autocomplete="off">
                        <i class="input-icon uil uil-at"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input type="password" name="password1" class="form-style" placeholder="Your Password" id="password1" v-model="password1" autocomplete="off">
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input type="password" name="password2" class="form-style" placeholder="Password Check" id="password2" v-model="password2" autocomplete="off">
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <div class="form-group mt-2">
                        <input type="date" name="birthday" class="form-style" id="birthday" v-model="birthday" autocomplete="off">
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <input type="submit" class="aclass logbtn mt-4" value="SignUp">
                    </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoSiview',
  data() {
    return {
      // login
      username: null,
      password: null,
      // sign up
      email: null,
      signusername: null,
      password1: null,
      password2: null,
      birthday: null,
      nickname: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      const email = ''

      const payload = {
        username: username,
        password: password,
        email : email,
      }
      this.$store.dispatch('login', payload)
    },
    signUp() {
      const username = this.signusername
      const password1 = this.password1
      const password2 = this.password2
      const birthday = this.birthday
      const nickname = this.nickname


      const payload = {
        username: username,
        password1: password1,
        password2: password2,
        birthday: birthday,
        nickname: nickname,
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style>

</style>
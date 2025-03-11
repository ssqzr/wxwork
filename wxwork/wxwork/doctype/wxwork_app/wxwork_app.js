// Copyright (c) 2025, ssqzr and contributors
// For license information, please see license.txt

frappe.ui.form.on("WXWork APP", {
    refresh(frm) {
        frm.wx_homepage_will_change = false
        frm.skip_before_save = false; // 防止重复提示
    },
    wx_company(frm) {
        frm.wx_homepage_will_change = true
    },
    wx_app_agentid(frm) {
        frm.wx_homepage_will_change = true
    },
    app_url(frm) {
        frm.wx_homepage_will_change = true
    },
    before_save(frm) {

        if (frm.is_new() || frm.skip_before_save)
            return;

        if (frm.is_dirty() && frm.wx_homepage_will_change) {
            frappe.validated = false;
            frappe.warn(
                __('请确认是否保存'),
                __('企业微信应用主页地址将改变，你需要重新配置企业微信应用的主页地址，否则应用将无法正常使用！</br></br>是否继续？'),
                () => {
                    frm.skip_before_save = true; // 防止重复提示
                    frm.save();
                },
                '继续',
                false
            )
        }
    }
});

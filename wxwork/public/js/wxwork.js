// 测试 $(document).ready 无效
// 应该是需要等元素渲染了才能查找到，那么执行代码的时机是什么时候呢？
// 暂时只找到这个时机，但是还是有问题，从大屏一点一点缩小到小屏，中间还是会出现问题，宽度缩小到一定程度才隐藏
// FIXME: https://github.com/frappe/frappe/issues/31648
$(document).on("list_sidebar_setup", function () {
    $(".layout-side-section").addClass("hidden-xs hidden-sm");
});
